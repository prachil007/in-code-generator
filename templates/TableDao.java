package ##package_name##.daos;

import java.util.List;

import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Component;

import ##package_name##.common.models.BaseModel;
import ##package_name##.models.##table_name_cs##;

@Component
public interface ##table_name_cs##Dao {

	public List<##table_name_cs##> findAll##table_name_cs_plural##();

    public ##table_name_cs## findBy##id_field_cs##(@Param("##id_field_lcs##") Long ##id_field_lcs##);

    public int add##table_name_cs##(##table_name_cs## ##table_name_lcs##);

    public int add##table_name_cs_plural##(@Param("##table_name_lcs_plural##") List<##table_name_cs##> ##table_name_lcs_plural##);

    public int update##table_name_cs##(##table_name_cs## ##table_name_lcs##);

    public int delete##table_name_cs##By##id_field_cs##(
        @Param("##id_field_lcs##") Long ##id_field_lcs##, @Param("baseModel") BaseModel baseModel);
}
