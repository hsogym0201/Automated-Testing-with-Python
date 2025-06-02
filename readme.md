# Tech Stack | 技术栈
- **Backend / 后端**: Python, Flask, Flask-RESTful
- **Framework / 测试框架**: unittest 
- **Database / 数据库**: SQLite (in-memory for testing)  
- **ORM / 对象关系映射**: SQLAlchemy <br><br>

# ArtfulArchive: An Art Collection Catalog System <br>| 艺术档案：艺术藏品收录系统
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
### - Unit Tests -
Unit tests focus on verifying the behavior of individual models in isolation. Each test ensures that object construction, field values, and internal methods.<br>
单元测试专注于模型本身的行为验证。测试内容包括对象的构造、属性赋值及方法（如 .json()）的输出是否符合预期。
Tested Models: ItemModel, StoreModel, UserModel<br><br>

### - Integration Tests - 
Integration tests ensure that the individual components (models and their relationships) interact correctly with each other and with the database.<br>
集成测试验证各模块（数据模型及其关系）之间的交互是否符合预期，确保与数据库的集成正确。
#### Item Integration Test
- Validates full CRUD (Create, Read, Update, Delete) functionality of ItemModel with persistent database state.<br>
ItemModel 的增删改查功能是否正常
- Ensures foreign key relationship correctness between items and stores.<br>
外键关系（item 与 store 之间）是否正确建立并保持一致性

#### Store Integration Test
- Tests the creation, deletion, and item relationships within StoreModel.<br>
StoreModel 的创建与删除功能是否有效, 以及StoreModel 与 ItemModel 的一对多关系是否构建正确
- Verifies that stores correctly return item lists in JSON format.<br>
Store 的 json() 方法是否正确返回嵌套的 item 数据

#### User Integration Test
- Tests whether a user can be saved and retrieved from the database using both ID and username.<br>
是否能通过用户名与用户ID在数据库中正确保存与检索<br><br>

### - System Tests -
System tests validate the full request–response cycle by simulating real HTTP calls to the API endpoints. <br>
系统测试通过模拟实际的 HTTP 请求调用接口，验证从请求到响应的完整流程。
#### Item System Test
- Tests item creation, retrieval, updating, and deletion through API endpoints.<br>
通过接口测试 Item 的创建、查询、更新和删除操作是否正常
- Validates error responses for missing stores or non-existent items.<br>
验证缺少关联商店或查询不存在商品时是否返回正确的错误响应

#### Store System Test
- Validates creation, deletion, and retrieval of stores via the API, including duplicate store handling.<br>
通过接口测试 Store 的创建、删除和查询功能，以及重复 Store 名称的处理逻辑
- Ensures item lists are correctly embedded in store responses.<br>
验证返回的 Store 数据中是否正确嵌套包含 item 列表

#### User System Test
- Tests user registration and login flows, ensuring valid tokens are returned.
测试用户注册与登录流程，确认是否返回有效的访问令牌（token）
- Checks for proper handling of duplicate registration attempts.
验证重复用户名注册时是否返回合理的错误信息
