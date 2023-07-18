pub struct WeightedBasis {
    pub k: usize,
    pub p: usize,
    pub knots: Vec<f64>,
    pub weights: Vec<f64>,
}

impl WeightedBasis {
    pub fn new(p: usize) -> Self {
        let k = p + 1;
        assert!(knots.len() == p + k + 1);
        assert!(p == knots.len());
        Self {
            k,
            p,
            knots: knots.clone(),
            weights: weights.clone(),
        }
    }
}
