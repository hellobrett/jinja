{{ '{%' }} set profile_store_staging_source = {{ config.profile_store_staging_source }} {{ '%}' }}
{{ '{%' }} set staging_schema_name = {{ config.staging_schema_name }} {{ '%}' }}
{{ '{%' }} set note_extract_table = {{ config.note_extract_table }} {{ '%}' }}
{{ '{%' }} set note_derivation_id = {{ config.note_derivation_id }} {{ '%}' }}
{{ '{%' }} set note_clean_table = {{ config.note_clean_table }} {{ '%}' }}
{{ '{%' }} set occurrence_date_origin = {{ config.occurrence_date_origin }} {{ '%}' }}
{{ '{%' }} set variable_type = {{ config.variable_type }} {{ '%}' }}

{% raw %}
WITH note_extractions_flattened AS (
    SELECT
        boc_note_id,
        extractions,
        VALUE:extracted:Value   AS extraction_value,
        MD5(VALUE)              AS extraction_id
    FROM {{ source(profile_store_staging_source, note_extract_table) }},
    LATERAL FLATTEN(input => extractions)
    WHERE extraction_value IS NOT NULL
)
SELECT
    note.boc_note_id                    AS id,
    note.source_encounter_id            AS encounter_id,
    note.boc_patient_id                 AS patient_id,
    extraction_id,
    note.note_recorded_dttm             AS recorded_datetime,
    recorded_datetime                   AS occurrence_datetime,
    TO_DATE(recorded_datetime)          AS occurrence_date,
    MONTH (occurrence_date)             AS occurrence_month,
    YEAR (occurrence_date)              AS occurrence_year,
    {{ occurrence_date_origin }}        AS occurrence_date_origin,
    note.boc_data_source_id             AS data_source_id,
    {{ note_derivation_id }}            AS derivation_id,
    ARRAY_CONSTRUCT(
    {{ evidence_source_object(staging_schema_name, note_extract_table, 'boc_note_id', 'id') }}
    )                                   AS sources,
    REPLACE (extraction_value, ' ', '') AS extraction_value_clean,
    {{ variable_type }}                 AS type
FROM note_extractions_flattened extract
JOIN {{ ref(note_clean_table) }} note
    ON extract.boc_note_id = note.boc_note_id
{% endraw %}