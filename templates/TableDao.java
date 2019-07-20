package ##package_name##.daos;

import org.springframework.stereotype.Component;
import org.apache.ibatis.annotations.Param;
import ##package_name##.models.##table_name_cs##;
import ##package_name##.common.models.BaseModel;

@Component
public interface ##table_name_cs##Dao {

    public ##table_name_cs## findBy##id_field_cs##(@Param("##id_field_lcs##") Long ##id_field_lcs##);

    public int add##table_name_cs##(##table_name_cs## ##table_name_lcs##);

    public int add##table_name_cs##s(@Param("##table_name_lcs##s") List<##table_name_cs##> ##table_name_lcs##s);

    public int update##table_name_cs##(##table_name_cs## ##table_name_lcs##);

    public int delete##table_name_cs##By##id_field_cs##(
        @Param("##id_field_lcs##") Long ##id_field_lcs##, @Param("baseModel") BaseModel baseModel);
}
