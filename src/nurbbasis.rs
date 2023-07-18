// TODO: Improve using https://isd.ktu.lt/it2010/material/Proceedings/1_AI_7.pdf

pub fn nurb_naive(u: f64, k: usize, p: usize, knots: &Vec<f64>) -> f64 {
    assert!(knots.len() >= p + k + 1);
    if u < knots[k] || u > knots[k + p + 1] {
        return 0.0;
    }
    if p == 0 {
        return 1.0;
    }
    let a = nurb_naive(u, k, p - 1, knots);
    let b = nurb_naive(u, k + 1, p - 1, knots);
    let c = (u - knots[k]) / (knots[k + p] - knots[k] + 1e-10);
    let d = (knots[k + p + 1] - u) / (knots[k + p + 1] - knots[k + 1] + 1e-10);
    return c * a +  d * b;
}

pub fn nurb_iterative(u: f64, k: usize, p: usize, knots: &Vec<f64>) -> f64 {
    assert!(knots.len() >= p + k + 1);
    let mut n: Vec<f64> = vec![0.0; p + 1]; // n uses j as index
    for _k in 0..=p {
        if u >= knots[k + _k] && u <= knots[k + _k + 1] {
            n[_k] = 1.0;
        }
    }
    for _p in 1..=p {
        for _k in 0..=p - _p {
            // Working on N[k+_k, _p]
            let c = (u - knots[k+_k]) / (knots[k + _k + _p] - knots[k + _k] + 1e-10);
            let d = (knots[k + _k + _p + 1] - u) / (knots[k + _k + _p + 1] - knots[k + _k + 1] + 1e-10);
            n[_k] = c * n[_k] + d * n[_k + 1];
        }
    }
    return n[0];
}
