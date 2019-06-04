# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('data_geracao', models.DateField()),
                ('hora_geracao', models.TimeField()),
                ('ano_eleicao', models.IntegerField()),
                ('num_turno', models.IntegerField()),
                ('descricao_eleicao', models.CharField(max_length=100)),
                ('sigla_uf', models.CharField(max_length=2)),
                ('sigla_ue', models.CharField(max_length=2)),
                ('descricao_ue', models.CharField(max_length=30)),
                ('codigo_cargo', models.IntegerField()),
                ('descricao_cargo', models.CharField(max_length=30)),
                ('nome_candidato', models.CharField(max_length=150)),
                ('sequencial_candidato', models.IntegerField()),
                ('numero_candidato', models.IntegerField()),
                ('cpf_candidato', models.IntegerField()),
                ('nome_urna_candidato', models.CharField(max_length=150)),
                ('cod_situacao_candidatura', models.IntegerField()),
                ('descricao_situacao_candidatura', models.CharField(max_length=30)),
                ('numero_partido', models.IntegerField()),
                ('sigla_partido', models.CharField(max_length=10)),
                ('nome_partido', models.CharField(max_length=80)),
                ('codigo_legenda', models.IntegerField()),
                ('sigla_legenda', models.TextField()),
                ('composicao_legenda', models.TextField()),
                ('nome_legenda', models.CharField(max_length=150)),
                ('codigo_ocupacao', models.IntegerField()),
                ('descricao_ocupacao', models.CharField(max_length=150)),
                ('data_nascimento', models.DateField()),
                ('num_titulo_eleitoral', models.IntegerField()),
                ('idade_data_eleicao', models.IntegerField()),
                ('codigo_sexo', models.IntegerField()),
                ('descricao_sexo', models.CharField(max_length=20)),
                ('cod_grau_instrucao', models.IntegerField()),
                ('descricao_grau_instrucao', models.CharField(max_length=60)),
                ('codigo_estado_civil', models.IntegerField()),
                ('descricao_estado_civil', models.CharField(max_length=30)),
                ('codigo_cor_raca', models.IntegerField()),
                ('descricao_cor_raca', models.CharField(max_length=30)),
                ('codigo_nacionalidade', models.IntegerField()),
                ('descricao_nacionalidade', models.CharField(max_length=60)),
                ('sigla_uf_nascimento', models.CharField(max_length=2)),
                ('codigo_municipio_nascimento', models.IntegerField()),
                ('nome_municipio_nascimento', models.CharField(max_length=100)),
                ('despesa_max_campanha', models.IntegerField()),
                ('cod_sit_tot_turno', models.IntegerField()),
                ('desc_sit_tot_turno', models.CharField(max_length=30)),
                ('email', models.TextField()),
            ],
        ),
    ]
