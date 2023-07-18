pub mod basis;
pub mod controlpoint;

use pyo3::prelude::*;

#[derive(Debug, Clone)]
#[pyclass]
pub struct Nurb {
    pub degree: usize,
    pub knots: Vec<f64>,
    #[pyo3(get)]
    pub control_points: Vec<controlpoint::ControlPoint>,
}

#[pymethods]
impl Nurb {
    #[new]
    pub fn new(degree: usize, knots: Vec<f64>, control_points: Vec<controlpoint::ControlPoint>) -> Self {
        assert!(control_points.len() == degree);
        assert!(knots.len() == control_points.len() + degree);
        // assert knots are sorted
        for i in 0..knots.len() - 1 {
            assert!(knots[i] <= knots[i + 1]);
        }
        // assert knots start with 0 and end with 1
        assert!(knots[0] == 0.0);
        assert!(knots[knots.len() - 1] == 1.0);
        Self {
            degree,
            knots,
            control_points,
        }
    }

    pub fn rasterize(&self, resolution: usize) -> Vec<controlpoint::ControlPoint> {
        let mut rasterized: Vec<controlpoint::ControlPoint> = Vec::with_capacity(resolution);
        for i in 0..resolution {
            let u = i as f64 / (resolution - 1) as f64;
            let mut cp = controlpoint::ControlPoint::new(0.0, 0.0, 0.0, 0.0);
            for j in 0..self.control_points.len() {
                let basis = basis::basis(u, j, self.degree, &self.knots);
                cp.x += basis * self.control_points[j].w * self.control_points[j].x;
                cp.y += basis * self.control_points[j].w * self.control_points[j].y;
                cp.z += basis * self.control_points[j].w * self.control_points[j].z;
                cp.w += basis * self.control_points[j].w * 1.0;
            }
            cp.normalize();
            rasterized.push(cp);
        }
        return rasterized;
    }

    pub fn rasterize_to_numpy<'py>(&self, py: Python<'py>, resolution: usize) -> &'py numpy::PyArray2<f32> {
        let points = self.rasterize(resolution);
        let mut result = numpy::ndarray::Array2::<f32>::zeros([resolution, 4]);
        for i in 0..resolution {
            result[[i, 0]] = points[i].x as f32;
            result[[i, 1]] = points[i].y as f32;
            result[[i, 2]] = points[i].z as f32;
            result[[i, 3]] = points[i].w as f32;
        }
        return numpy::PyArray2::from_owned_array(py, result);
    }
}