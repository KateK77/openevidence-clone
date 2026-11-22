# Fixture review (setup only; not CUA outcomes)

Live hosted deployment confirmed through Render read-only deployment listing: c903b65ce3f8f49fe72416ca8948d215a0690a49, dep-dbtbu4p9aqoc73akvgl0.

Application source for query_language.py, rag.py, views.py and serializers.py is unchanged from this deployed SHA. Glossary maps 糖尿病 to diabetes mellitus; 脊髓空洞症 is not mapped. Unmapped Han causes empty normalized query, no PubMed query, no source context and synthesize exits before calling a model. This documented source inspection is used only to bound provider effects, never as CUA PASS evidence.

Reviewed README, docs, settings and fixture requirements for a pre-existing public latency/fault fixture. No isolated controllable-delay endpoint, separate unconfigured evaluation instance, or documented browser-accessible fixture control was found. Public service remains configured. No production configuration was changed.

First 70 records remain untouched. 71–90 are newly authorized retests because old execution artifacts were not recovered. Old reported totals are retained separately and are not used to determine these outcomes.
