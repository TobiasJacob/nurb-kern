use pyo3::{prelude::*, types::PyList};

use crate::nurbbasis;

#[pyfunction]
pub fn nurb_naive(u: f64, k: usize, p: usize, knots: &PyList) -> f64 {
    let knots = knots.extract::<Vec<f64>>().unwrap();
    return nurbbasis::nurb_naive(u, k, p, &knots)
}
#[pyfunction]
pub fn nurb_iterative(u: f64, k: usize, p: usize, knots: &PyList) -> f64 {
    let knots = knots.extract::<Vec<f64>>().unwrap();
    return nurbbasis::nurb_iterative(u, k, p, &knots)
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn nurbkern(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(nurb_naive, m)?)?;
    m.add_function(wrap_pyfunction!(nurb_iterative, m)?)?;
    Ok(())
}
