

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

CREATE TABLE `user` {
    user_id bigint NOT NULL,
    first_name bigint,
    last_name bigint,
    email text,
    CONSTRAINT user_pk_user_id PRIMARY KEY user(user_id)
}