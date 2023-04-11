-- based on standards here: https://om1inc.atlassian.net/wiki/spaces/PROD/pages/1670250739/Standards+for+Structured+Curated+Extracted+Estimated+Disease+Activity+PRO+Outcomes+Variables
{{ '{{' }}
    dedupe(partitionByColumns=['patient_id', 'encounter_id', 'TO_DATE(recorded_datetime)', 'occurrence_date', 'occurrence_year', 'occurrence_month', 'extraction_value_clean'],
           orderByColumns=['recorded_datetime DESC', 'occurrence_datetime DESC', 'occurrence_date_origin DESC'],
           fromTableRef=ref('{{ config.variable_name }}_extractions_staged'))
{{ '}}' }}