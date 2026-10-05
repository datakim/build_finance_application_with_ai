-- Listing 5.1 (chapter 5): A simplified SQL script to unify BFSI partial marts.
-- Run by the create_credit_data_mart task in ../airflow_dag_credit_pipeline.py (listing 5.2).
CREATE OR REPLACE VIEW credit_data_mart AS
SELECT
  u.user_id,
  u.month,
  COALESCE(u.total_spend, 0) AS monthly_spend,
  b.bureau_score,
  b.delinquency_flag,
  d.region,
  d.age_bracket,
  d.tokenized_kyc
FROM monthly_usage u
LEFT JOIN bureau_lookup b
       ON u.user_id = b.user_id
      AND u.month   = b.month
LEFT JOIN demographics d
       ON u.user_id = d.user_id;
