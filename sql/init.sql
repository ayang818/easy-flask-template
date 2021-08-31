create database pf_base;

-- 测试表
create table if not exists base_test (
    id int unsigned AUTO_INCREMENT comment "主键",
    create_time timestamp not null default CURRENT_TIMESTAMP comment "创建时间",
    update_time  timestamp not null ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP comment "更新时间",
   primary key(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 多群组租户信息
create table if not exists pf_group_info (
    id int unsigned AUTO_INCREMENT comment "租户id",
    group_name varchar(255) not null comment "租户名称",
    create_time timestamp not null default CURRENT_TIMESTAMP comment "创建时间",
    update_time  timestamp not null ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP comment "更新时间",
   primary key(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
insert into pf_group_info(group_name) values('测试组织'); -- 测试组织默认为 1

-- 用户基础信息
create table if not exists pf_user_info  (
    id int unsigned  comment "user_id; 与 pf_user_secret_info 中 id 相同",
    nick_name varchar(255) not null comment "昵称",
    secret_info_id int unsigned not null comment "敏感信息表user_id",
    group_id int unsigned not null comment "对应的租户",
    create_time timestamp not null default CURRENT_TIMESTAMP comment "创建时间",
    update_time  timestamp not null ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP comment "更新时间",
   primary key(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- 用户敏感信息
create table if not exists pf_user_secret_info (
    id int unsigned AUTO_INCREMENT comment "user_id",
    username varchar(255) not null comment "用户名;全局唯一",
    password varchar(255) not null comment "密码",
    salt varchar(255) not null comment "密码撒盐",
    create_time timestamp not null default CURRENT_TIMESTAMP comment "创建时间",
    update_time  timestamp not null ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP comment "更新时间",
   primary key(id),
   unique key uidx_username(username)
)ENGINE=InnoDB AUTO_INCREMENT=10000 DEFAULT CHARSET=utf8mb4;
insert into pf_user_secret_info(username, password, salt) values("1234567", "9d9a542f5a676e0c1e19654f28d069aa", "salt");
insert into pf_user_info(nick_name, secret_info_id, group_id) values("yfc", 1, 1);