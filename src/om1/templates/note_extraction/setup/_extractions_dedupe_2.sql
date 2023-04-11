{{ '{{' }}
    dedupe(partitionByColumns=['patient_id', 'occurrence_year', 'occurrence_month', 'extraction_value_clean'],
           orderByColumns=['recorded_datetime DESC', 'occurrence_datetime DESC', 'occurrence_date_origin DESC'],
           fromTableRef=ref('{{ config.variable_name }}_extractions_dedupe_1'))
{{ '}}' }}