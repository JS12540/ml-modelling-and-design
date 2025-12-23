# ml-modelling-and-design
ML Modelling and design problems


## Classification Report Metrics Explained

This classification report includes **macro average** and **weighted average** scores, which are useful when working with imbalanced datasets.

### Macro Average
- Computes precision, recall, and F1-score **independently for each class**
- Takes the **simple average** across all classes
- **All classes are treated equally**, regardless of how many samples they have

**Use case:**  
Helps understand how well the model performs on *each class on average*, especially important for minority classes.

---

### Weighted Average
- Computes metrics per class
- Averages them **weighted by the number of samples in each class**
- Classes with more samples have **greater influence** on the final score

**Use case:**  
Reflects the model’s **overall performance on the dataset**, but can hide poor performance on rare classes.

---

### Note on Imbalanced Data
In highly imbalanced datasets, weighted averages may appear very high even if the model performs poorly on minority classes. Macro averages provide better visibility into this issue.

# Macro Average vs Weighted Average in Classification Metrics

Consider a binary classification problem with an imbalanced dataset:

| Class | Support | Precision | Recall | F1-score |
|-------|---------|-----------|--------|----------|
| 0     | 90      | 1.00      | 1.00   | 1.00     |
| 1     | 10      | 0.50      | 0.60   | 0.55     |

**Total samples:** 100

---

## Macro Average

Macro average treats **all classes equally**, regardless of their size.

### Formula
```
Macro Avg = (Metric_class_0 + Metric_class_1) / Number_of_classes
```

### Example Calculation

- **Macro Precision** = (1.00 + 0.50) / 2 = **0.75**
- **Macro Recall** = (1.00 + 0.60) / 2 = **0.80**
- **Macro F1-score** = (1.00 + 0.55) / 2 = **0.775**

### Use Case

Best for evaluating performance on minority classes.

---

## Weighted Average

Weighted average accounts for **class imbalance** by weighting each class by its number of samples.

### Formula
```
Weighted Avg = (Metric_0 × Support_0 + Metric_1 × Support_1) / Total_samples
```

### Example Calculation

- **Weighted Precision** = (1.00 × 90 + 0.50 × 10) / 100 = **0.95**
- **Weighted Recall** = (1.00 × 90 + 0.60 × 10) / 100 = **0.96**
- **Weighted F1-score** = (1.00 × 90 + 0.55 × 10) / 100 = **0.955**

### Use Case

Reflects overall dataset performance, but may hide poor results on rare classes.

---

## Key Takeaway

- **Macro average** highlights minority class performance
- **Weighted average** reflects overall performance influenced by majority classes
