import os

from jinja2 import Environment, FileSystemLoader

from noteextractiontemplater import NoteExtractionTemplater

# Demo Config
config = {
    "variable_name": "EASI",
    "source": "note_extraction",
    "profile_store_staging_source": "'enriched_profile_store_staging_extractions'",
    "staging_schema_name": "'PROFILE_STORE_STAGING'",
    "note_extract_table": "'easi__extraction__single_note'",
    "note_derivation_id": "35",
    "note_clean_table": "'note_clean'",
    "occurrence_date_origin": "'recorded date'",
    "variable_type": "'EASI - Eczema Area and Severity Index'",
}

templater = NoteExtractionTemplater()
templater.write_models(config)
