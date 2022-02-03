import jenkins

server = jenkins.Jenkins('http://host.docker.internal:8080', username='xxxx', password='xxxx')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
print(server.jobs_count())
server.create_job('test-job-3', jenkins.EMPTY_CONFIG_XML)
jobs = server.get_jobs()
print(jobs)
my_job = server.get_job_config('test-job-3')
print(my_job)
server.build_job('test-job-3')
server.disable_job('test-job-3')
server.copy_job('test-job-3', 'test-job-4')
server.enable_job('test-job-4')
server.reconfig_job('test-job-4', jenkins.RECONFIG_XML)




