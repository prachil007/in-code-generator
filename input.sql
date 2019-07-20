

create table new_object (
    new_object_id bigint not null,
    'name' text,
    address_line_field1 varchar(100),
    address_line_field2 varchar(100),
    deleted boolean,
    created_by bigint not null,
    created_at bigint not null,
    updated_by bigint not null,
    updated_at bigint not null
);

