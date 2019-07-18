package com.yourcompany.yourappname.daos;

import org.springframework.stereotype.Component;
import org.apache.ibatis.annotations.Param;
import com.yourcompany.yourappname.models.NewObject;
import com.mobisoftinfotech.common.models.BaseModel;

@Component
public interface NewObjectDao {

    public NewObject findByNewObjectId(@Param("newObjectId") Long newObjectId);

    public int addNewObject(NewObject newObject);

    public int addNewObjects(@Param("newObjects") List<NewObject> newObjects);

    public int updateNewObject(NewObject newObject);

    public int deleteNewObjectByNewObjectId(
        @Param("newObjectId") Long newObjectId, @Param("baseModel") BaseModel baseModel);
}
