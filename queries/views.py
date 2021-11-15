from random import sample

from dbserver.Core.DBConnect import check_query
from datetime import datetime
from dbserver.models import ControlWork, ExecControlWork, Query, DataScheme
from .forms import ControlWorkForm
from django.shortcuts import render
from django.http import HttpResponseRedirect


def all_control_works(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')

    control_works = ControlWork.objects.all()
    return render(request, 'all_control_works.html',
                  {'control_works': control_works})


def control_work(request, control_work_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')

    control_work_id = int(control_work_id)

    if not ControlWork.objects.filter(pk=control_work_id).exists():
        return HttpResponseRedirect('/queries')

    control_work_ = ControlWork.objects.get(pk=control_work_id)

    if not ExecControlWork.objects.filter(control_work=control_work_,
                                          user=request.user).exists():
        all_control_work_queries = Query.objects.filter(query_scheme=control_work_.control_scheme).order_by("?")
        numbers = range(0, len(all_control_work_queries))
        user_sample = sample(numbers, 3)

        exec_control_work = ExecControlWork(
            user=request.user,
            control_work=control_work_,
            start_time=datetime.now(),
            end_time=datetime.now(),
            query_1=all_control_work_queries[user_sample[0]],
            query_2=all_control_work_queries[user_sample[1]],
            query_3=all_control_work_queries[user_sample[2]],
        )
        exec_control_work.save()
    else:
        exec_control_work = ExecControlWork.objects.get(control_work=control_work_,
                                                        user=request.user)

    if not exec_control_work.done:
        if request.method == 'POST':
            form = ControlWorkForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                if request.POST.get('save'):
                    print("save")
                    exec_control_work.query_1_answer = cd.get("query_1_answer")
                    exec_control_work.query_2_answer = cd.get("query_2_answer")
                    exec_control_work.query_3_answer = cd.get("query_3_answer")
                    exec_control_work.end_time = datetime.now()
                    exec_control_work.save()
                elif request.POST.get('done'):
                    print("done")
                    exec_control_work.query_1_answer = cd.get("query_1_answer")
                    exec_control_work.query_2_answer = cd.get("query_2_answer")
                    exec_control_work.query_3_answer = cd.get("query_3_answer")
                    exec_control_work.end_time = datetime.now()
                    exec_control_work.done = True
                    exec_control_work.save()

                    # TODO: ТУТ ОБЯЗАТЕЛЬНО НУЖЕН ФИЛЬТР UPDATE, DELETE и ПРОЧЕГО КАЛА !!!!!!!!!!!

                    result, error = check_query(reference_code=exec_control_work.query_1.query_answer,
                                                user_code=exec_control_work.query_1_answer,
                                                database=request.user.database)
                    if error:
                        result = "При проверке запроса возникла ошибка. " \
                                 "Обратитесь к системному администратору. (Ошибка: {})".format(error)
                    exec_control_work.query_1_result = result

                    result, error = check_query(reference_code=exec_control_work.query_2.query_answer,
                                                user_code=exec_control_work.query_2_answer,
                                                database=request.user.database)
                    if error:
                        result = "При проверке запроса возникла ошибка. " \
                                 "Обратитесь к системному администратору. (Ошибка: {})".format(error)
                    exec_control_work.query_2_result = result

                    result, error = check_query(reference_code=exec_control_work.query_3.query_answer,
                                                user_code=exec_control_work.query_3_answer,
                                                database=request.user.database)
                    if error:
                        result = "При проверке запроса возникла ошибка. " \
                                 "Обратитесь к системному администратору. (Ошибка: {})".format(error)
                    exec_control_work.query_3_result = result

                    # exec_control_work.query_1_result = "OK"
                    # exec_control_work.query_2_result = "Ошибка: запрос выдал больше строк, чем ожидалось."
                    # exec_control_work.query_3_result = "Ошибка: запрос выдал меньше строк, чем ожидалось."
                    exec_control_work.save()
                    return HttpResponseRedirect('/queries/{}'.format(control_work_id))
        else:
            form = ControlWorkForm()
        return render(request, 'control_work.html',
                      {'form': form,
                       'exec_control_work': exec_control_work})
    else:
        return render(request, 'control_work_done.html',
                      {'exec_control_work': exec_control_work})
