{{ '{{' }}
    resolve_conflicts(makeDistinctColumn='extraction_value_clean',
                     partitionByColumns=['patient_id', 'encounter_id', 'TO_DATE(recorded_datetime)', 'occurrence_month', 'occurrence_year'],
                     fromTableRef=ref('{{ config.variable_name }}_extractions_dedupe_2'))
{{ '}}' }}