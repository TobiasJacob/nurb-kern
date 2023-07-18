// TODO: Improve using https://isd.ktu.lt/it2010/material/Proceedings/1_AI_7.pdf

pub fn naive_basis(u: f64, k: usize, p: usize, knots: &Vec<f64>) -> f64 {
    assert!(knots.len() > p + k);
    if u < knots[k] || u > knots[k + p] {
        return 0.0;
    }
    if p == 1 {
        return 1.0;
    }
    let a = naive_basis(u, k, p - 1, knots);
    let b = naive_basis(u, k + 1, p - 1, knots);
    let c = (u - knots[k]) / (knots[k + p - 1] - knots[k] + 1e-10);
    let d = (knots[k + p] - u) / (knots[k + p] - knots[k + 1] + 1e-10);
    return c * a +  d * b;
}

pub fn basis(u: f64, k: usize, p: usize, knots: &Vec<f64>) -> f64 {
    assert!(knots.len() > p + k);
    let mut n: Vec<f64> = vec![0.0; p]; // n uses j as index
    for _k in 0..p {
        if u >= knots[k + _k] && u <= knots[k + _k + 1] {
            n[_k] = 1.0;
        }
    }
    for _p in 2..=p {
        for _k in 0..=p - _p {
            // Working on N[k+_k, _p]
            let c = (u - knots[k + _k]) / (knots[k + _k + _p - 1] - knots[k + _k] + 1e-10);
            let d = (knots[k + _k + _p] - u) / (knots[k + _k + _p] - knots[k + _k + 1] + 1e-10);
            n[_k] = c * n[_k] + d * n[_k + 1];
        }
    }
    return n[0];
}
