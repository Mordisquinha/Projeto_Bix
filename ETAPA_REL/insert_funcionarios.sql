insert into rel.funcionarios (id_funcionario, funcionario, insercao_base)
select  stg.funcionarios.id_funcionario 
		,stg.funcionarios.funcionario
        ,CURDATE()
from stg.funcionarios 
left join rel.funcionarios on
rel.funcionarios.id_funcionario = stg.funcionarios.id_funcionario 
where rel.funcionarios.exclusao_logica is null
and rel.funcionarios.insercao_base is null
;
