========
Analysis
========

Analysis是一个辅助分析应用性能的工具，通过加载中间件可以获取每个请求处理过程中所有执行的数据库操作。

注意： 只在 settings.DEBUG 为 True 才会生效。

快速开始
----

1. 添加 "analysis" 到settings配置的 INSTALLED_APPS 中：
    INSTALLED_APPS = (
        ...
        'analysis',
    )

2. 添加 analysis 的中间件到settings配置的 MIDDLEWARE_CLASSES (django 1.10 以上版本为 MIDDLEWARE) 中：
    MIDDLEWARE_CLASSES = (
        'analysis.middleware.SQLAnalysisMiddleware',
        ...
    )
    尽可能放到最上边以得到更精确的数据。

3. 添加 analysis 的 URLConf 到你项目的 urls.py 文件中：
    url(r'^analysis/', include('analysis.urls')),

4. 启动应用后，通过 http://example.com/analysis/ 访问分析数据。