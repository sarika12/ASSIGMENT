from bottle import route, run, template, get, post, request,delete,put
p_dict={}
info=[]

@post('/patient')
def add_patient():
    p_id = request.POST['id']
    p_name = request.POST['name']
    p_gender = request.POST['gender']
    p_age = request.POST['age']
    p_address = request.POST['address']
    p_phone = request.POST['phone']
	

    info = ' '.join([p_name,p_gender,p_age,p_address,p_phone])
    p_dict.update({p_id:info})
	

    return p_dict

@get('/patient_show')
def show_patient():
    p_id = request.POST['id']
    if p_id not in p_dict.keys():
        return 'This is not a correct patient id'
    else:
        return p_dict[p_id]

@put('/patient_update')
def patient_update():
    p_id = request.POST['id']
    p_name = request.POST['name']
    p_gender = request.POST['gender']
    p_age = request.POST['age']
    p_address = request.POST['address']
    pa_phone = request.POST['phone']
    info = ' '.join([p_name,p_gender,p_age,p_address,pa_phone])
    p_dict.update({p_id:info})
    return p_dict
   


@delete('/patient_delete')
def delete_patient():
    p_id = request.POST['id']
    p_dict.pop(p_id)
    return p_dict


run(host='localhost',port=8080)
