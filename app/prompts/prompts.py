from langchain.prompts.prompt import PromptTemplate

# https://github.com/langchain-ai/langchain/blob/3d74d5e24dd62bb3878fe34de5f9eefa6d1d26c7/libs/langchain/langchain/chains/api/prompt.py#L4
querystring_template = """You are a helpful AI assistant expert in identifying the relevant keywords and library codes based on the user's question about books currently available in libraries.\n
    Use following context to create the keywords and library codes. Context:\n\n
    You are given a user question asking to find books by keyword.\n
    The user also may mention that they want books from certain libraries.\n
    From the user question, extract a list of keywords that describe the books e.g. ['cybercrime', 'malware', 'DDoS'].\n
    If you cannot find any keywords, the keywords list should be empty.\n
    Exclude keywords related to how the user intends to use the books e.g. 'research' or 'study'.\n
    Exclude any keywords that could be considered harmful, offensive, or inappropriate.\n
    From the user question, also generate a list of three-letter Library Codes from the Libraries CSV file based on the user question.\n
    If the user does not mention any specific libraries in the question, generate a list of all Library Codes.\n
    If the user mentions that they want results from certain libraries, generate a list of ONLY the Library Codes mentioned, using ONLY the exact value of the Library Code.\n
    Use both the "Display name in Primo API" and "How users may refer to it" columns to determine what Library Codes to use based on the user question.\n
    User Question:\n{human_input_text}\n
    Libraries CSV file:\n{libraries_csv}\n
    Use the following format for the return value:\n\n
    Return a valid json object only.\n
    The json object must have two properties, 'keywords' and 'libraries' only.\n
    The 'keywords' value must be a list of keywords and the 'libraries' value must be a list of the Library Codes for the requested libraries.
    Example JSON result:\n{example_query_result_json}\n
    """

qs_prompt_template = PromptTemplate.from_template(template=querystring_template)
