# Artifact-Driven Metadata Schema Development

This repository contains the source code and evidence artifacts for
*Artifact-Driven Metadata Schema Development: A Human-in-the-Loop Methodology
with Multimodal LLMs*.

It reproduces the paper's schema-development case study: metadata discovery,
field-profile aggregation, canonical concept synthesis, expert refinement,
concept coverage assessment, operational schema design, and two held-out
validation exercises. Annotation, layout-model benchmarking, and downstream
metadata extraction are intentionally excluded.

## Install

Python 3.10 or newer and [uv](https://docs.astral.sh/uv/) are recommended.

```shell
uv sync --extra notebooks --extra dev
cp .env.example .env
```

Add an OpenAI API key to `.env` only when rerunning model calls. The checked-in
artifacts support analysis without API access.

## Data

The images and document metadata are stored in
[`ai4data/data-snapshot`](https://huggingface.co/datasets/ai4data/data-snapshot).
The exact paper samples are frozen in `data/manifests/`.

```shell
uv run python scripts/fetch_data.py
```

## Reproduce the reported analyses

Run notebooks in this order:

1. `notebooks/schema_discovery/2.0-analysis.ipynb`
2. `notebooks/schema_discovery/3.0-initial_profiling.ipynb`
3. `notebooks/schema_discovery/4.1-results_viewer.ipynb`
4. `notebooks/schema_discovery/5.0-canonical_field_frequency_analysis.ipynb`
5. `notebooks/schema_discovery/7.0-eda_for_paper.ipynb`
6. `notebooks/schema_validation1/3.0-schema_validation1_analysis.ipynb`
7. `notebooks/schema_validation1/3.1-schema_validation1_viewer.ipynb`
8. `notebooks/schema_validation2/2.0-schema_validation2_analysis.ipynb`

These notebooks read the checked-in files under `artifacts/`. The raw
Responses API outputs are retained because rerunning an LLM is not expected to
produce byte-identical results.

## Rerun model-supported stages

The execution notebooks are:

- `notebooks/schema_discovery/1.0-schema_discovery.ipynb`
- `src/schema_development/concept_synthesis.py`
- `notebooks/schema_discovery/4.0-field_labeling_using_ontology.ipynb`
- `notebooks/schema_validation1/2.0-schema_validation1.ipynb`
- `notebooks/schema_validation2/1.0-schema_validation2.ipynb`

Fresh outputs are written under `runs/`, which is gitignored. Model names,
reasoning effort, prompts, frozen schemas, and Structured Output contracts are
preserved, but API availability and nondeterminism may affect a fresh run.

## Human decisions

LLM outputs are candidates, not schema decisions. The refined concept inventory
is `artifacts/discovery/3.1-ontology_v1.csv`; the adjudicated profile mapping is
`artifacts/discovery/4.2-final_labeled_field_profiles.csv`; and the validation
reports record why proposed gaps were accepted, rejected, or treated as
representation limitations. See `docs/schema_design_decisions.md` for the
41-concept to 36-field operational design step.

## Appendix H

`supplement/appendix_h/` reproduces the paper's post-study comparison with the
later machine-readable v1.2 schema. It is supplemental and does not alter the
main case-study evidence. Its runner uses
`artifacts/appendix_h/evaluated_schema_v1.2.schema.json`, the exact pre-amendment
contract used by that run.

The package and notebook names retain `validation3` as a historical internal
label for this Appendix H post-study comparison. Canonical prompts and
configuration live under `src/schema_development/validation3/`.

## Tests

```shell
uv run pytest -q
```

## License

Code is released under the MIT License. Source documents and snapshot images
remain subject to their original providers' terms.
