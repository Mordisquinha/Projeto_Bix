insert into rel.vendas (id_venda, id_funcionario, id_categoria, data_venda, venda, insercao_base)
select  stg.vendas.id_venda, stg.vendas.id_funcionario
		,stg.vendas.id_categoria
		,stg.vendas.data_venda
		,stg.vendas.venda
        ,CURDATE()
from stg.vendas 
left join rel.vendas on
rel.vendas.id_venda = stg.vendas.id_venda 
where rel.vendas.exclusao_logica is null
and rel.vendas.insercao_base is null;
