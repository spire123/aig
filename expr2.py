diseases = {
    'Common Cold': ['sore throat', 'runny nose', 'cough', 'fever'],
    'Flu': ['fever', 'body aches', 'headache', 'cough'],
    'Stomach Flu': ['diarrhea', 'vomiting', 'abdominal cramps', 'fever'],
    'Migraine': ['headache', 'nausea', 'sensitivity to light and sound'],
    'Pneumonia': ['cough', 'fever', 'difficulty breathing', 'chest pain'],
    'Hypertension': ['high blood pressure', 'headache', 'dizziness', 'chest pain'],
    'Asthma': ['wheezing', 'shortness of breath', 'coughing', 'chest tightness'],
    'Diabetes': ['frequent urination', 'increased thirst', 'blurred vision', 'fatigue'],
   
}

remedies = {
    'Common Cold': ['Rest', 'Hydration', 'Over-the-counter medications for symptoms'],
    'Flu': ['Rest', 'Hydration', 'Antiviral medications'],
    'Stomach Flu': ['Rest', 'Hydration', 'Oral rehydration solutions', 'Antidiarrheal medications'],
    'Migraine': ['Rest in dark room', 'Pain relievers', 'Triptans'],
    'Pneumonia': ['Antibiotics', 'Rest', 'Hydration', 'Pain relievers'],
    'Hypertension': ['Lifestyle changes', 'Medications', 'Regular blood pressure monitoring'],
    'Asthma': ['Inhaled corticosteroids', 'Bronchodilators', 'Lifestyle changes'],
    'Diabetes': ['Blood sugar monitoring', 'Insulin therapy', 'Lifestyle changes'],
}

print("************* Medical Expert System ****************")
print("Please enter your symptoms separated by commas:")
user_symptoms = input("You: ").lower().split(',')

possible_diseases = []
for disease, symptoms in diseases.items():
    if any(symptom in user_symptoms for symptom in symptoms):
        possible_diseases.append(disease)

if len(possible_diseases) == 0:
    print("Your symptoms are unclear. Please consult a medical professional.")
else:
    print("Expert System: ")
    print("Possible diseases:")
    for disease in possible_diseases:
        print(disease)
        print("Remedies:")
        for remedy in remedies[disease]:
            print(remedy)
        print('\n')