package ##package_name##.services;

import javax.validation.Valid;
import javax.validation.constraints.NotNull;

import org.apache.ibatis.annotations.Param;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.validation.annotation.Validated;

import ##package_name##.common.models.BaseModel;
import ##package_name##.daos.##table_name_cs##Dao;
import ##package_name##.models.##table_name_cs##;

@Service
@Validated
public class ##table_name_cs##Service {
 
    @Autowired
    private ##table_name_cs##Dao ##table_name_lcs##Dao;

    @Transactional(rollbackFor = Exception.class)
    public List<##table_name_cs##> findAll##table_name_cs_plural##() {
		return ##table_name_lcs##Dao.findAll##table_name_cs_plural##();
	}

    @Transactional(rollbackFor = Exception.class)
    public ##table_name_cs## findBy##id_field_cs##
        (@NotNull(message = "required.##id_field_lcs##") Long ##id_field_lcs##) {
        return ##table_name_lcs##Dao.findBy##id_field_cs##(##id_field_lcs##);
    }
    
    @Validated
    @Transactional(rollbackFor = Exception.class)
    public int add##table_name_cs##(
        @Valid ##table_name_cs## ##table_name_lcs##,
        @NotNull(message = "required.loggedInUserId") Long loggedInUserId) {
        ##table_name_lcs##.updateCCUU(loggedInUserId);
        return ##table_name_lcs##Dao.add##table_name_cs##(##table_name_lcs##);
    }
    
    @Validated
    @Transactional(rollbackFor = Exception.class)
    public int update##table_name_cs##(
        @Valid ##table_name_cs## ##table_name_lcs##,
        @NotNull(message = "required.loggedInUserId") Long loggedInUserId) {
        ##table_name_lcs##.updateUU(loggedInUserId);
        return ##table_name_lcs##Dao.update##table_name_cs##(##table_name_lcs##);
    }
    
    @Transactional(rollbackFor = Exception.class)
    public int delete##table_name_cs##By##id_field_cs##(
        @NotNull(message = "required.##id_field_lcs##") @Param("##id_field_lcs##") Long ##id_field_lcs##,
        @NotNull(message = "required.loggedInUserId") Long loggedInUserId) {

        BaseModel baseModel = new BaseModel();
        baseModel.updateUU(loggedInUserId);
        return ##table_name_lcs##Dao.delete##table_name_cs##By##id_field_cs##(##id_field_lcs##, baseModel);
    }
}
