insert into rel.categorias (id_categoria, categoria, insercao_base)
select  stg.categorias.id_categoria  
		,stg.categorias.categoria 
        ,CURDATE()
from stg.categorias 
left join rel.categorias on
rel.categorias.id_categoria = stg.categorias.id_categoria 
where rel.categorias.exclusao_logica is null
and rel.categorias.insercao_base is null;

