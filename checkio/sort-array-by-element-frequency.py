   path('', views.index, name='home'),
    path('list_data', views.list_data, name='data'),
    path('list_agrdb', views.list_data, name='agrdb'),
    path('list_calendb', views.list_data, name='calendb'),
    path('list_docsdb', views.list_data, name='docsdb'),
    path('list_dodb', views.list_data, name='dodb'),
    path('list_eboradoc', views.list_data, name='eboradoc'),
    path('list_ebzdb', views.list_data, name='ebzdb'),
    path('list_econtdb', views.list_data, name='econtdb'),
    path('list_edodb', views.list_data, name='edodb'),
    path('list_epzSupport', views.list_data, name='epzSupport'),
    path('list_eruzfs', views.list_data, name='eruzfs'),
    path('list_fksBus', views.list_data, name='fksBus'),
    path('list_fksFs', views.list_data, name='fksFs'),
    path('list_fkszdb', views.fkszdb, name='fkszdb'),
    path('list_fz223main', views.list_data, name='fz223main'),
    path('list_fz223odb', views.list_data, name='fz223odb'),
    path('list_infradb', views.list_data, name='infradb'),
    path('list_ktrudb', views.list_data, name='ktrudb'),
    path('list_lkpfs', views.list_data, name='lkpfs'),
    path('list_lkpmain', views.list_data, name='lkpmain'),
    path('list_pgzdb', views.list_data, name='pgzdb'),
    path('list_phonedb', views.list_data, name='phonedb'),
    path('list_ppansi', views.list_data, name='ppansi'),
    path('list_rdikdb', views.list_data, name='rdikdb'),
    path('list_rpgzdb', views.list_data, name='rpgzdb'),
    path('list_techdb', views.list_data, name='techdb'),
    path('list_tsupdb', views.list_data, name='tsupdb'),


    {% extends 'main/layout.html' %}

{% block title %}Список БД{% endblock %}

{% block data %}
    <div class="items">
        <h1>
        <ul>
            <a href="{% url 'fkszdb' %}"><li>ANONYMOUS</li></a>
            <a href="{% url 'dodb' %}"><li>БД dodb ДО</li></a>
            <a href="{% url 'eboradoc' %}"><li>БД eboradoc Хранилище файлов УЗ</li></a>
            <a href="{% url 'ebzdb' %}"><li>БД ebzdb УЗ РК РБГ</li></a>
            <a href="{% url 'econtdb' %}"><li>БД econtdb ПЗК</li></a>
            <a href="{% url 'edodb' %}"><li>БД edodb ЭДО</li></a>
            <a href="{% url 'epzSupport' %}"><li>БД epzSupport ФКС ОЧ ЕПЗ</li></a>
            <a href="{% url 'eruzfs' %}"><li>БД eruzfs ЕРУЗ ХФ</li></a>
            <a href="{% url 'fksBus' %}"><li>БД fksBus Шина</li></a>
            <a href="{% url 'fksFs' %}"><li>БД fksFs Хранилище файлов ФКС</li></a>
            <a href="{% url 'fkszdb' %}"><li>БД fkszdb ЗЧ ФКС</li></a>
            <a href="{% url 'fz223main' %}"><li>БД fz223main ЗЧ 223</li></a>
            <a href="{% url 'fz223odb' %}"><li>БД fz223odb ЕПЗ старая</li></a>
            <a href="{% url 'infradb' %}"><li>БД infradb ЕГРЮЛ ЕГРИП</li></a>
            <a href="{% url 'ktrudb' %}"><li>БД ktrudb КТРУ ЗЧ</li></a>
            <a href="{% url 'lkpfs' %}"><li>БД lkpfs ЛКП ХФ</li></a>
            <a href="{% url 'lkpmain' %}"><li>БД lkpmain ЛКП</li></a>
            <a href="{% url 'pgzdb' %}"><li>БД pgzdb ППА НСИ Контр. реестры</li></a>
            <a href="{% url 'phonedb' %}"><li>БД phonedb Мобилка</li></a>
            <a href="{% url 'ppansi' %}"><li>БД ppansi ППА НСИ</li></a>
            <a href="{% url 'rdikdb' %}"><li>БД rdikdb РДИК</li></a>
            <a href="{% url 'rpgzdb' %}"><li>БД rpgzdb РПГЗ</li></a>
            <a href="{% url 'techdb' %}"><li>БД techdb Тех поддержки на x86</li></a>
            <a href="{% url 'tsupdb' %}"><li>БД tsupdb ЛКО</li></a>
        </ul>
        </h1>
    </div>
{% endblock %}

{% extends 'main/layout.html' %}

{% block title %}Список БД{% endblock %}

{% block data %}
    <div class="items">
        <h1>
        <ul>
            <a href="{% url 'agrdb' %}"><li>БД agrdb РД 615</li></a>
            <a href="{% url 'calendb' %}"><li>БД calendb Календарь</li></a>
            <a href="{% url 'docsdb' %}"><li>БД docsdb Документов</li></a>
            <a href="{% url 'dodb' %}"><li>БД dodb ДО</li></a>
            <a href="{% url 'eboradoc' %}"><li>БД eboradoc Хранилище файлов УЗ</li></a>
            <a href="{% url 'ebzdb' %}"><li>БД ebzdb УЗ РК РБГ</li></a>
            <a href="{% url 'econtdb' %}"><li>БД econtdb ПЗК</li></a>
            <a href="{% url 'edodb' %}"><li>БД edodb ЭДО</li></a>
            <a href="{% url 'epzSupport' %}"><li>БД epzSupport ФКС ОЧ ЕПЗ</li></a>
            <a href="{% url 'eruzfs' %}"><li>БД eruzfs ЕРУЗ ХФ</li></a>
            <a href="{% url 'fksBus' %}"><li>БД fksBus Шина</li></a>
            <a href="{% url 'fksFs' %}"><li>БД fksFs Хранилище файлов ФКС</li></a>
            <a href="{% url 'fkszdb' %}"><li>БД fkszdb ЗЧ ФКС</li></a>
            <a href="{% url 'fz223main' %}"><li>БД fz223main ЗЧ 223</li></a>
            <a href="{% url 'fz223odb' %}"><li>БД fz223odb ЕПЗ старая</li></a>
            <a href="{% url 'infradb' %}"><li>БД infradb ЕГРЮЛ ЕГРИП</li></a>
            <a href="{% url 'ktrudb' %}"><li>БД ktrudb КТРУ ЗЧ</li></a>
            <a href="{% url 'lkpfs' %}"><li>БД lkpfs ЛКП ХФ</li></a>
            <a href="{% url 'lkpmain' %}"><li>БД lkpmain ЛКП</li></a>
            <a href="{% url 'pgzdb' %}"><li>БД pgzdb ППА НСИ Контр. реестры</li></a>
            <a href="{% url 'phonedb' %}"><li>БД phonedb Мобилка</li></a>
            <a href="{% url 'ppansi' %}"><li>БД ppansi ППА НСИ</li></a>
            <a href="{% url 'rdikdb' %}"><li>БД rdikdb РДИК</li></a>
            <a href="{% url 'rpgzdb' %}"><li>БД rpgzdb РПГЗ</li></a>
            <a href="{% url 'techdb' %}"><li>БД techdb Тех поддержки на x86</li></a>
            <a href="{% url 'tsupdb' %}"><li>БД tsupdb ЛКО</li></a>
        </ul>
        </h1>
    </div>
{% endblock %}


еис 6 - https://eis6.lanit.ru/epz/main/public/home.html
еис 7 - https://eis7.lanit.ru/epz/main/public/home.html
еис 4 - https://eis4.roskazna.ru/epz/main/public/home.html
еис 5 - https://eis5.roskazna.ru/epz/main/public/home.html


Главная Портал Закупок
https://eis6.lanit.ru


Главная Портал Закупок
https://eis7.lanit.ru



{% extends 'main/layout.html' %}

{% block title %}Список БД{% endblock %}
{% block data %}

<body>
{% load mptt_tags %}
<ul>
    {% recursetree lists %}
        <li>
            <font size="#ffffff" color="white" face="Arial" >
            <a href="{{ node.get_absolute_url }}">{{ node.name }}</a>
            {% if not node.is_leaf_node %}
                     </font>
                <ul class="children" >
                    {{ children }}
                </ul>
            {% endif %}

        </li>
    {% endrecursetree %}
</ul>
</body>
{% endblock %}