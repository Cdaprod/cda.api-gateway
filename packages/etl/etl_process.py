from code_context import CodeContext

class ETLProcess:
    def __init__(self, code, text):
        self.context = CodeContext(code, text)
        self.metadata = None
        self.tokenized_code = None
        self.cleaned_text = None
        self.combined_data = None

    async def run(self):
        # Run ETL methods sequentially or asynchronously as required
        await self.extract()  # Extract metadata
        await self.transform()  # Tokenize code and clean text
        await self.load()  # Combine all data

    async def extract(self):
        # Extract metadata from code
        self.metadata = self.context.extract_metadata(self.context.code)
        print("Metadata extracted:", self.metadata)

    async def transform(self):
        # Tokenize the code and clean text
        self.tokenized_code = self.context.tokenize_code(self.context.code)
        self.cleaned_text = self.context.clean_text(self.context.text)
        print("Code tokenized:", self.tokenized_code)
        print("Text cleaned:", self.cleaned_text)

    async def load(self):
        # Combine all the data
        self.combined_data = {
            "metadata": self.metadata,
            "tokenized_code": self.tokenized_code,
            "cleaned_text": self.cleaned_text
        }
        print("Combined data:", self.combined_data)
        
        if __name__ == "__main__":
#     code_snippet = """
#    def example_function(arg1, arg2):
#     return arg1 + arg2
# """


		with open('data.py', 'r') as file:
		    code_snippet = file.read()
					'''
					This is not an adequate way to handle the data
					TODO: Use "Code" object in  for Code object
					'''
				
    surrounding_text = "This function adds two numbers."

    etl_process = ETLProcess(code_snippet, surrounding_text)
    asyncio.run(etl_process.run())