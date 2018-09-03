
def calc_patient_wait_time(n):
    # let num_of_patient be the number of patients
    num_of_patient = len(n)
    
    # let total_wait_minutes be total patient wait minutes
    total_wait_minutes = 0
    
    # let num_of_patients_treated be number of patients treated
    num_of_patients_treated = 0
    
    # initerate n items
    for i in num_of_patient:
        num_of_patients_treated += 1
        # total_wait_minutes += (this item wait minute * num_of_untreated_patients)
        total_wait_minutes += i * (num_of_patient - num_of_patients_treated)
        
    # function return
    return total_wait_minutes


if __name__ == '__main__':
    n = [5, 10, 15]
    print(calc_patient_wait_time(n))
    # result is 20
