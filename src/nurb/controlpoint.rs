// structure to define control points
use pyo3::prelude::*;

#[derive(Debug, Clone)]
#[pyclass]
pub struct ControlPoint {
    pub x: f64,
    pub y: f64,
    pub z: f64,
    pub w: f64,
}

#[pymethods]
impl ControlPoint {
    #[new]
    pub fn new(x: f64, y: f64, z: f64, w: f64) -> ControlPoint {
        ControlPoint { x, y, z, w }
    }

    pub fn normalize(&mut self) {
        self.x /= self.w;
        self.y /= self.w;
        self.z /= self.w;
        self.w = 1.0;
    }
}