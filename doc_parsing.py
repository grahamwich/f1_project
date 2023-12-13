from pdfminer.high_level import extract_text
import os

def pdf_to_text(pdf_path):
    try:
        # Extract text from the PDF file
        text = extract_text(pdf_path)
        return text

    except Exception as e:
        print(f"Error: {e}")
        return None


# data preproccessing:
def preprocess(text):
    # use regex to get:
    # name, car_number, opposing_car, overall_time, time_penalty, location, penalty_points, session, reason, ISC_code

    # NN data needed: time_penalty (will be used with frames)
    pass

# pdf conversion
general_path = 'f1_penalty_documents/'
for file in os.listdir(general_path):
    if file.endswith(".pdf"):
        pdf_file_path = general_path + file
        text = pdf_to_text(pdf_file_path)
        print(text)
        # preproccess text

# code in text now, will want to split more things later but for right now, only split the time penalty:


# place all time penalties within a list to pair with a frames tuple
time_penalties = []




# track 2 cars across a turn,      assign to a time penalty
# [distances across # of frames] : 00:05 (5 seconds)

# account for speed? turn #?