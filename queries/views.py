from random import randint
from dbserver.models import AST
from dbserver.models import ControlWork, ExecControlWork
from .forms import ControlWorkForm
from django.shortcuts import render
from django.http import HttpResponseRedirect


def all_control_works(request):
    if request.user.is_authenticated:
        # all_user_schemas = request.user.data_schemas.split()
        # return render(request, 'all_control_works.html',
        #               {'img_1': 'img/' + all_user_schemas[0] + '.jpg',
        #                'img_2': 'img/' + all_user_schemas[1] + '.jpg',
        #                'img_3': 'img/' + all_user_schemas[2] + '.jpg'})
        control_works = ControlWork.objects.all()
        return render(request, 'all_control_works.html',
                      {'control_works': control_works})
    else:
        return HttpResponseRedirect('/account/login/')


def control_work(request, control_work_id):
    control_work_id = int(control_work_id)
    if request.user.is_authenticated:

        if not ControlWork.objects.filter(pk=control_work_id).exists():
            return HttpResponseRedirect('/queries')

        control_work_ = ControlWork.objects.get(pk=control_work_id)

        if not ExecControlWork.objects.filter(control_work=control_work_, user=request.user):


        # all_user_schemas = request.user.data_schemas.split()
        # schema = all_user_schemas[control_work_id - 1]
        #
        # all_queries = AST.objects.all()
        # all_sec_queries = all_queries.values('db_index', 'db_request')
        #
        # random_three_queries = []
        # for i in range(3):
        #     random_three_queries.append(all_sec_queries[randint(0, len(all_sec_queries) - 1)])
        # print(random_three_queries)

        if request.method == 'POST':
            form = ControlWorkForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                print(cd)
                # ТУТ ДОЛЖНО БЫТЬ ЧТО-ТО ПОЛЕЗНОЕ
                # ТУТ ДОЛЖНО БЫТЬ ЧТО-ТО ПОЛЕЗНОЕ
                # ТУТ ДОЛЖНО БЫТЬ ЧТО-ТО ПОЛЕЗНОЕ
                # ТУТ ДОЛЖНО БЫТЬ ЧТО-ТО ПОЛЕЗНОЕ
                # ТУТ ДОЛЖНО БЫТЬ ЧТО-ТО ПОЛЕЗНОЕ
                # ТУТ ДОЛЖНО БЫТЬ ЧТО-ТО ПОЛЕЗНОЕ
                # ТУТ ДОЛЖНО БЫТЬ ЧТО-ТО ПОЛЕЗНОЕ

                # TODO: сделать так:
                '''
                При отправке ответов сохранять в таблицу с контрольными работами
                запись о том, что пользователь уже это решал и отвечал. Мб добавить
                туда еще и оценку, надо подумать.
                Если пользователь первый раз, он просто решает и отправляет ответ.
                Если пользователь не первый раз и в базе уже есть его решение, просто
                вывести ему его решение без возможности повторной отправки.
                '''
                # TODO: В МОДЕЛЬ ДОЛЖНО БЫТЬ ПОЛЕ С АЙДИ ЗАПРОСА!!!!!!!!!
        else:
            form = ControlWorkForm()

        return render(request, 'control_work.html',
                      {'form': form,
                       'control_work_id': control_work_id,
                       'img': 'img/' + all_user_schemas[control_work_id - 1] + '.jpg',
                       'random_three_queries': random_three_queries})
    else:
        return HttpResponseRedirect('/account/login/')
