from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
    
from agent.tools.search_lundbeck import vector_store

urls = [
    "https://www.lundbeck.com/us/our-focus/community-engagement/grants-and-contributions",
    "https://www.lundbeck.com/us/our-focus/neurology",
    "https://www.lundbeck.com/us/our-focus/neurology/lennox-gastaut-syndrome",
    "https://www.lundbeck.com/us/our-focus/neurology/migraine",
    "https://www.lundbeck.com/us/our-focus/psychiatry/agitation-in-alzheimers-dementia",
    "https://www.lundbeck.com/us/our-focus/psychiatry/bipolar-disorder",
    "https://www.lundbeck.com/us/our-focus/psychiatry/borderline-personality-disorder",
    "https://www.lundbeck.com/us/our-focus/psychiatry/depression",
    "https://www.lundbeck.com/us/our-focus/psychiatry/generalized-anxiety-disorder",
    "https://www.lundbeck.com/us/our-focus/psychiatry/post-traumatic-stress-disorder",
    "https://www.lundbeck.com/us/our-focus/psychiatry/schizophrenia",

    "https://www.lundbeck.com/us/our-science/research-and-development",
    "https://www.lundbeck.com/us/our-science/research-and-development/our-value-chain",
    "https://www.lundbeck.com/us/our-science/products",
    "https://www.lundbeck.com/us/our-science/pipeline",
    "https://www.lundbeck.com/us/our-science/medical-education",
    "https://www.lundbeck.com/us/our-science/medical-education/Lundbeck-Institute",
    "https://www.lundbeck.com/us/our-science/clinical-trials",
    "https://www.lundbeck.com/us/our-science/clinical-trials/expanded-access-policy",
    "https://www.lundbeck.com/us/our-science/clinical-trials/clinical-trial-diversity",
    "https://www.lundbeck.com/us/our-science/clinical-data-sharing",

    "https://www.lundbeck.com/content/lundbeck-com/global/global-site/en/sustainability.html",
    "https://www.lundbeck.com/global/sustainability/access-to-brain-health",
    "https://www.lundbeck.com/global/sustainability/climate-action",
    "https://www.lundbeck.com/global/sustainability/donations-and-grants",
    "https://www.lundbeck.com/global/sustainability/health-and-safety-at-work",
    "https://www.lundbeck.com/global/sustainability/materials-use-and-waste",
    "https://www.lundbeck.com/global/sustainability/responsible-business-conduct",
    "https://www.lundbeck.com/global/sustainability/suppliers-and-third-parties",
    "https://www.lundbeck.com/global/sustainability/transparent-interactions",

    "https://www.lundbeck.com/global/about-us",
    "https://www.lundbeck.com/global/about-us/our-commitment",
    "https://www.lundbeck.com/global/about-us/our-commitment/diversity-and-inclusion",
    "https://www.lundbeck.com/global/about-us/our-commitment/our-position-on-brain-health",
    "https://www.lundbeck.com/global/about-us/our-commitment/our-osition-on-patient-centricity",
    "https://www.lundbeck.com/global/about-us/this-is-lundbeck",
    "https://www.lundbeck.com/global/about-us/this-is-lundbeck/at-a-glance",
    "https://www.lundbeck.com/global/about-us/this-is-lundbeck/organization-and-ownership",
    "https://www.lundbeck.com/global/about-us/this-is-lundbeck/the-lundbeck-foundation",

    "https://www.lundbeck.com/global/about-us/this-is-lundbeck/our-history",
    "https://www.lundbeck.com/global/about-us/our-leadership",
    "https://www.lundbeck.com/global/about-us/our-leadership/executive-management",
    "https://www.lundbeck.com/global/about-us/our-leadership/board-of-directors",
    "https://www.lundbeck.com/global/about-us/corporate-governance",
    "https://www.lundbeck.com/global/about-us/corporate-governance/board-tasks",
    "https://www.lundbeck.com/global/about-us/corporate-governance/remuneration",
    "https://www.lundbeck.com/global/about-us/corporate-governance/risk-management",
]

docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=500, chunk_overlap=0
)
docs_splits = text_splitter.split_documents(docs_list)

vector_store.add_documents(docs_splits)

