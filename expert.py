print("--------->> Medical and Hospital Expert System <<--------")
print("---------------------------------------------------------")
def expert_system(symptoms,symptom1):
    diagnosis = None
    treatment = None

    if (symptoms == 'fever' and symptom1 == 'cough') or (symptoms == 'cough' and symptom1 == 'fever'):
        diagnosis = 'Migraine'
        treatment = 'Ibuprofen'
        hospitals='Recommended Hospitals:\n 1. Life Care \n >> Facilaties: 1. X-ray 2. Blood Test  3. cash payment\n2. Apollo  Hospital:\n >> Facilities: 1.Mri 2.CT-Scan online as well as cash'
        return diagnosis, treatment, hospitals

    elif (symptoms == 'cough' and symptom1 == 'headache') or (symptoms == 'headache' and symptom1 == 'cough') :
        diagnosis = 'Flu'
        treatment = 'Acetaminophen'
        hospitals='Recommended Hospitals:\n 1. Life Care \n >> Facilaties: 1. X-ray 2. Blood Test 3. cash payment\n2. Apollo  Hospital:\n>> Facilities: 1.Mri 2.CT-Scan online as well as cash'
        return diagnosis, treatment,hospitals
    
    elif (symptoms == 'chest_pain' and symptom1 == 'fever') or (symptoms == 'fever' and symptom1 == 'chest_pain'):
        diagnosis = 'pneumonia'
        treatment = 'Antibiotics and rest'
        hospitals = 'Recommended Hospitals:\n 1. Ashoka \n >> Facilaties: 1. X-ray 2. Blood Test 3. cash payment\n2. wokart  Hospital:\n >>Facilities: 1.Mri 2.CT-Scan online as well as cash'
        return diagnosis, treatment,hospitals
    
    elif (symptoms == 'shortness_of_breadth' and symptom1 == 'cough') or (symptoms == 'cough' and symptom1 == 'shortness_of_breadth') :
        diagnosis = 'Asthma'
        treatment = 'Bronchodilators and inhaled corticosteroids'
        hospitals = 'Recommended Hospitals:\n 1. Six sigma \n >> Facilaties: 1. X-ray 2. Blood Test 3.cash payment\n2. magna  Hospital:\n >>Facilities: 1.Mri 2.CT-Scan online as well as cash'
        return diagnosis, treatment,hospitals
    
    elif (symptoms == 'frequent_urination'  and symptom1 == 'fatigue') or (symptoms == 'fatigue'  and symptom1 == 'frequent_urination'):
        diagnosis = 'Diabetes'
        treatment = 'Insulin therapy and blood sugar monitoring'
        hospitals = 'Recommended Hospitals:\n 1. cooper \n >> Facilaties: 1. X-ray 2. Blood Test 3.cash payment\n2. leelavati Hospital:\n >>Facilities: 1.Mri 2.CT-Scan online as well as cash'
        return diagnosis, treatment,hospitals
    else:
        diagnosis='No diagnosis'
        treatment="No treatment"
    return diagnosis, treatment


symptoms= input("Enter the symptom : ")
symptom1=input("Enter the symptom : ")



diagnosis, treatment, hospitals = expert_system(symptoms,symptom1)

print("---------------------------------------------------------")
print('Diagnosis:', diagnosis)
print("---------------------------------------------------------")
print('Treatment:', treatment)
print("---------------------------------------------------------")
print(hospitals)