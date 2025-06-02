# Tech Stack | 技术栈
- **Backend / 后端**: Python, Flask, Flask-RESTful
- **Framework / 测试框架**: unittest 
- **Database / 数据库**: SQLite (in-memory for testing)  
- **ORM / 对象关系映射**: SQLAlchemy <br><br>

# ArtfulArchive: An Art Collection Catalog System | 艺术档案：艺术藏品收录系统
## Overview | 概述
A lightweight RESTful API built with Flask and SQLAlchemy for galleries, private collectors and art fairs. ArtfulArchive allows users to add, query, and remove art pieces, and track ownership information. With a clean and expandable structure, it's ready for future enhancements like image management, artist profiles.<br>
一个基于Flask和SQLAlchemy构建的轻量级RESTful API，面向广大艺术馆、私人收藏家和艺术博览会。ArtfulArchive允许用户添加、查询和删除艺术品，并跟踪所有权信息。系统结构清晰，易于后续进行图片管理、艺术家资料等功能的扩展。

## API Endpoints | API 端点
- /item/<string:name>      [HTTP Methods: get, post, delete, put]
- /items      [HTTP Methods: get]
- /store/<string:name>      [HTTP Methods: get, post, delete]
- /stores      [HTTP Methods: get]
- /register      [HTTP Methods: post]
- /auth      [HTTP Methods: post]

## The Testing Pyramid | 测试覆盖
This project includes a comprehensive test suite covering unit tests, integration tests and system tests, ensuring the robustness and correctness of API functionality and data models.<br>
本项目涵盖单元测试、集成测试和系统测试，确保API功能和数据模型的健壮性和正确性。
### - unit tests -


### - integration tests - 

### - system tests -
