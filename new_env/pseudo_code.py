#to summarize the pdf based on user

# Import requried libraries/modules
#upload the document to the folder

# #load the docuement
# def load(pdf_file):
#     # loading the docuemnt
#     pass

#function to split docuemnt based on pages
def split_document(document_path):
    # split the source document into multiple output documents based on pages
    #save the document to the output folder
    #path to save the files
    return files_path
#create a list contaning doc_id

#load the fiels that are in local directory

def laod_files(file_path):
    #load the fiels from the input file path
    pass
    return list_files
    

#function to extract txt form document and store it in a txt or pdf file

#intialize the llama and embedding models
def modles(llama2,emebd_model):
    #setting  the llama2models and embedding models 
    pass
    
#summerize the document and genrating embeddings
def summerize_index(list_files,modles):
    #genrating the summary document based on doc_id
    #genrating the embeddings
    pass
 
#store the index to vector data base
def store_vectordb(index):
    #store the sumamrized fiels and embedding to the vectoredb
    pass

#reteive the question from each index through llama index( get_doc_sumamry)
 def questions_extract(sumamry_index_nodes):
    #pass the doc_id to the doc_summary_index to genrate the question related to the doc_id
    #extrcat the questions and save to the list/dict
    pass
    return list_questions

#llm model to fetch the questions 
def questions_fetching(list_question):
    #using llm model fetch teh question based on user
    pass
    return user_questions

#pass the retriver and extracted question to set the contex window
def prompt(retriver_node,user_questions):
    #pass the userquery,set the context window

#pass this context window to llama models---genrate a sumamry for each questions
#concate the genrated summary
def process_summarized_doc(document_path):

    split_the_file=split_document(document_path)
    laod_the file= laod_files(split_the_file)
    #genrate the sumamry
    summerize_doc_index=summaerize_index(models,load_the_files)
    vectoredb=store_vectordb(summerize_doc_index)
    questions_extraction=questions_extract(summerize_doc_index)
    llm_question_fetcing=questions_fetching( questions_extraction)
    inference_summary={summerize_doc_index,
                       llm_question_fetching,
                       context}
   return inference_summary

document_path = "path/to/your/document.pdf"
result = process_summarized_doc(document_path)
print(result)




