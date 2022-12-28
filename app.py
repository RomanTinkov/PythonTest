from flask import Flask, render_template, send_from_directory
import os
import sys

app = Flask(__name__)

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

@app.route('/download/<path:path>', methods=['GET'])
def static_proxy(path):
    return send_from_directory(root, path)

@app.route('/')
def index():
    #response = app.response_class(
    #    response='updateCenter.post({"connectionCheckUrl":"https://www.google.com/","core":{"buildDate":"Nov 30, 2022","name":"core","sha1":"rXv2mv73ObnkYof6xMS5P1b7vCs=","sha256":"6Wrn9Z2KAJvb81UdXp+s2X/4ptQEx+okOO8meYjVNCc=","size":93555446,"url":"https://updates.jenkins.io/download/war/2.375.1/jenkins.war","version":"2.375.1"},"deprecations":{},"generationTimestamp":"2022-12-28T16:55:26Z","id":"default","plugins":{"warnings-ng":{"buildDate":"Dec 14, 2022","defaultBranch":"master","dependencies":[{"name":"analysis-model-api","optional":false,"version":"10.21.0"},{"name":"bootstrap5-api","optional":false,"version":"5.2.1-2"},{"name":"checks-api","optional":false,"version":"1.8.0"},{"name":"commons-lang3-api","optional":false,"version":"3.12.0-36.vd97de6465d5b_"},{"name":"commons-text-api","optional":false,"version":"1.10.0-27.vb_fa_3896786a_7"},{"name":"data-tables-api","optional":false,"version":"1.12.1-4"},{"name":"echarts-api","optional":false,"version":"5.4.0-1"},{"name":"font-awesome-api","optional":false,"version":"6.2.1-1"},{"name":"forensics-api","optional":false,"version":"1.15.1"},{"name":"jquery3-api","optional":false,"version":"3.6.1-2"},{"name":"plugin-util-api","optional":false,"version":"2.20.0"},{"name":"prism-api","optional":false,"version":"1.29.0-1"},{"name":"pull-request-monitoring","optional":true,"version":"1.7.8"},{"name":"workflow-api","optional":false,"version":"1200.v8005c684b_a_c6"},{"name":"workflow-cps","optional":false,"version":"3536.vb_8a_6628079d5"},{"name":"workflow-job","optional":false,"version":"1207.ve6191ff089f8"},{"name":"workflow-step-api","optional":false,"version":"639.v6eca_cd8c04a_a_"},{"name":"antisamy-markup-formatter","optional":false,"version":"155.v795fb_8702324"},{"name":"apache-httpcomponents-client-4-api","optional":false,"version":"4.5.13-138.v4e7d9a_7b_a_e61"},{"name":"credentials","optional":false,"version":"1143.vb_e8b_b_ceee347"},{"name":"dashboard-view","optional":true,"version":"2.466.vdfefd95a_b_f8d"},{"name":"jackson2-api","optional":false,"version":"2.13.4.20221013-295.v8e29ea_354141"},{"name":"matrix-project","optional":true,"version":"772.v494f19991984"},{"name":"structs","optional":false,"version":"324.va_f5d6774f3a_d"},{"name":"token-macro","optional":true,"version":"308.v4f2b_ed62b_b_16"}],"developers":[{"developerId":"drulli","name":"Ulli Hafner"}],"excerpt":"Collects compiler warnings or issues reported by static analysis tools and visualizes the results. It has built-in support for many compilers (cpp, clang, java, ...) and tools (spotbugs, pmd, checkstyle, eslint, phpstan, ...), see the list of <a href=\"https://github.com/jenkinsci/warnings-ng-plugin/blob/master/SUPPORTED-FORMATS.md\" target=\"_blank\" rel=\"nofollow noopener noreferrer\">supported report formats</a>.","gav":"io.jenkins.plugins:warnings-ng:9.22.0","issueTrackers":[{"reportUrl":"https://www.jenkins.io/participate/report-issue/redirect/#24526","type":"jira","viewUrl":"https://issues.jenkins.io/issues/?jql=component=24526"}],"labels":[],"name":"warnings-ng","popularity":23886,"previousTimestamp":"2022-12-07T10:10:16.00Z","previousVersion":"9.21.0","releaseTimestamp":"2022-12-14T13:42:58.00Z","requiredCore":"2.346.3","scm":"https://github.com/jenkinsci/warnings-ng-plugin","sha1":"D39zgtRvzyULbX+/KSp2vgjatno=","sha256":"t41IV+HzmvR/ox04d+K8MG5yE44v51u+PNAle0CbHgY=","size":11611865,"title":"Warnings Next Generation","url":"https://updates.jenkins.io/download/plugins/warnings-ng/9.22.0/warnings-ng.hpi","version":"9.22.0","wiki":"https://plugins.jenkins.io/warnings-ng"}},"signature":{"certificates":["MIIFYTCCA0kCBQDerb7+MA0GCSqGSIb3DQEBDQUAMIGKMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTERMA8GA1UEBwwIU2FuIEpvc2UxGDAWBgNVBAoMD0plbmtpbnMgUHJvamVjdDEaMBgGA1UEAwwRS29oc3VrZSBLYXdhZ3VjaGkxHTAbBgkqhkiG9w0BCQEWDmtrQGtvaHN1a2Uub3JnMB4XDTIyMDYwMTA3MTMxNloXDTIzMDYwMTA3MTMxNlowXjELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExGDAWBgNVBAoMD0plbmtpbnMgUHJvamVjdDEgMB4GA1UEAwwXQ29tbXVuaXR5IFVwZGF0ZSBDZW50ZXIwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQC8Zs2Fw0XQjrB2fNQjRMMBYgApa75KeIvNgK38JGc9xiY/JgSLgCkzNMe3QZG8jwUsOO3CGRfp9M5S2pAxPhcGinWh7bbYAfuIpzbWZ6f+qFi17HPuwUQJmPOC+kZmxKwj1CezPpFZHRduQuQPf5E0EQdLHSF/FDcEOxYJEitBkJbD3OybbA1QDbu2mz77LKio1ZOCp6SuX6LB4N0ySZMEu5nJoCs3ISVS32Q8poVQkvMmB6MHof7Xs7Hkx5hajHOonMdqC027Q1sqHn5GoK1VTOYiOloRolKeH6Xszd28vTmeCMSu0TI4UNzIW+E5YgCt9O6qzV7eve4J7a4s7RT4R/aoUvPhDVavaxuUTJvFtBX+szYXygj6jNGKWsR3TZyIrqFvs+OQdWs9AZtSe0mI3xoeRyM4K6ELIblHXRpdzUsoeV48jMnegHqagtXAwTdUeki0LUMVo7dMk/Ek9Bl29WL8MvVXQ4um2NPzyI/NDzkVYWK7UlPxKlj6ewMyXHWpeCAsV5PwzfQnE5dH36g5oX5o2vVp5laEJbWpgacKtM4z6PlDYEVy6NsvSY4Q4WJRcf0+oW8B39AAK+39mjgqJ6ezp47p9m/l/2VZNqc4nrVB9RdOWdOXEfASbK3BWh6TG99QSnOmhDwlY8PVyqSYlXZriRug32qqHsSGpzcBCQIDAQABMA0GCSqGSIb3DQEBDQUAA4ICAQBniEu2FNft21CAFvtXsFFvBsto0wvRI0130W3i18viTrMCSWO/1gdov69mERzXq7HBV7Co2XKDXjANswMIeCIu4NokpZgvQPju7YNKMV3BG5/dD6hC2eHC26pXZiM3JqzLmk21ZzjY0DRT0Ol41GADEGEdn8Ost54Gj6ORpdyCG17cWpogrnokgr9vw9ZftvtcXiuv2SJYYzq/AYE8yl1iocIJKL5ylpWYGx15bGUu3H0rWRsZJMxhq1rZVphiXGFkNCjzkl8pdfb1t0zgZtAk2ywxrUwH85BObJIM6vvBx/tGcoOOpK0Z2BeSoLlh7eaQp08VNjjp0ARkEnC6v8dvjqrbxkjdoSfiH2mIpbTzqF6VuiVw2vVvGZ8hgfx5hinHNkjQAdaVzS+YEXHmb4dD4t6ImvPtYo+dlib+nqjMgQL7PgA6tMJgL47IFOSFXKBUdja9rHkdhrMAcJpbt35KWOkjx51sd23ddHDomfu6lijOADKsk8FCECKFjhiVf2yFxSmtyMEk1OLNDWDQHTdEcGkeXHW7IuBUCYjxAtv52ltTrmk/AMd8udtbV22yVq5RPX4lYUxSFMSadmZzHYCA/eZeD5ohn1vETWqzuHLJArBNRRCTvwlM3xKrVgZZzBlIJh/MqeQOiOkUYCPo+ImerTyjmwLJFGR/wb9zwLOpPg=="],"correct_digest":"Zc3/EMcmAb8BO5onnxtN7Sf2wiU=","correct_digest512":"8141729fd07eaa849754bd748059e97ab7bc530fb3847da52769cf14ed8a01d53840e64291b3f1d147d2253bcc436e91c35a67ccd4b7a1ade862988e1211f908","correct_signature":"INz3xVTb3SesfXtklYaUk2cIV5IY9YRwXT92IfevjN4s9tSU9gG9KuloegRYT4wyxi8RBSsHrx/wVCgIKO7Ka8yA/Zb0gYbGzJ2OEGHOdEa2yDqUzlae5jNVdto2GoPfCYLNWX4kls/U56ZLZP6QcDvbUHxubSB0aW292YgSteLSJa5ZALoLzDgeHpoHgfhtw4yYxMtnh3CAlb39K1edJ8HDWIIdhdGa35wxauFjIwKFpFEJx/pGjj3NWvzPfDgWDSSLJJC7oTxkiqVJJAlWmz1O09qhLrrUFBbfTMp3/TNJnMDSM0pW15PRYCrdbsQnEyTuOm+tG+exGSuiewM0l8/KVpu7MmozqdpSAxuYRgpTYdhteT1Kx46js+XBm3g0c6/GzTMBBN5wE49Y/yQ4cqPYn+IOQVxBzASnZCLfWwtnx6/pqNX/rnRWjxUstToedLai7ZLyuTh7WtiUH7pzNXShCR8cV5kxyhmUzrPqepu8RZnIMPzg3kbq6wwaQHp7O2zT8pBnPUTGaVUvqgvinCA1LlRtPFtGS8kgvJQvG8jBohJeSqzM/A6fOimQj15aH67C4DfhMXyjY4AnzUnWlVyMSnZ7LUKY7ocBn9rwuLOauVlybKihrihN5gBWgcK1fdHbdYmzZxyIh2rSk/vExTp4OfXZMc9k2gbxVbaNFB4=","correct_signature512":"54e2bbe00585cb48242f6629fe4bb1283411f3befa4d9bd108a9546da6153757551a34a4ab0e15533cbeda7c6ac993910f70e933874ca5ed11f8e3892b65743ed2c14876662215610855d230e2043cb7244169b2548ee4f137d36c83ca6f0124bd93f60cb66fecd34f80811024752b97dd8dcdc4a84a615b86c97446f331ad3f458b8117317430d8cf3b948bb3911fd489a9fd017a1152247ad5b3f724d558fd3d52fb52440c16156f96aa66555318841da85ec58e5257b697362a601d893f88c4162e9c8ce8377029c754a5f633c59c5a761d7c3f5e199de2b4d2fa63dc623dc5df22c55721b1b722b5fa1ad6281d7a9a59ccc6915e862f1a6369b7cbe2d77d1cb6c1a218fae1322b3bb4ba6b0a13b3ec1158bbc8ee0ec9c8c6b26f80d4ac5975985cba4c8157d7d728261048ea2d3643a8c7e4b217457b4370711417e9ead47d7358526cbd41f6f1bfc2fdefe349e35fbf3a136cd8566c0175ffa9014f4c677f7bf3455546b1ac232fde76e8d67eb9e03681370407d0f4cbc507cb43af48dbea0c9a604034a9564f68715be8c1c195d695516b988cbca6afd1684f27e83ea752669941015e3da22d33123bd93053d18f6b32871704e694ea6fab05ae204cbd98ce5dc08da06eb94baef7b26d57b360693c543af86aff8ffab3f08b4850968230da1379fde8ee04b55bb20d8c855c3777f93e1e465b29c4d6c7dd745f939446"},"updateCenterVersion":"1","warnings":[]});',
    #    status=200,
    #    mimetype='application/json'
    #)
    return root
    #return response




if __name__ == '__main__': app.run(debug=True)
