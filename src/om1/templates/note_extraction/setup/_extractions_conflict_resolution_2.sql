{{ '{{' }}
    resolve_conflicts(makeDistinctColumn='extraction_value_clean',
                     partitionByColumns=['patient_id', 'occurrence_year', 'occurrence_month'],
                     fromTableRef=ref('{{ config.variable_name }}_extractions_conflict_resolution_1'))
{{ '}}' }}