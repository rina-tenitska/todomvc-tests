from jenkins/jenkins:lts
# Switch to user root
USER root
# Install docker
RUN curl -fsSL https://get.docker.com -o get-docker.sh \
    && sh get-docker.sh
# Install docker-compose
RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose
# Add user jenkins to docker group
RUN usermod -aG docker jenkins
# Start docker
RUN service docker start
#Switch to user jenkins
USER jenkins
# Add plugins
RUN jenkins-plugin-cli --plugins allure-jenkins-plugin:latest \
    build-timeout:latest \
    credentials-binding:latest \
    timestamper:latest \
    ws-cleanup:latest \
    workflow-aggregator:latest \
    github-branch-source:latest \
    pipeline-github-lib:latest \
    pipeline-stage-view:latest \
    git:latest \
    email-ext:latest \
    mailer:latest \
    matrix-auth:latest \
    pam-auth:latest \
    ldap:latest
# Configure Allure plugin using groovy script
COPY init.groovy.d/ /var/jenkins_home/init.groovy.d/
# Add template for email notification
COPY email-html.template /var/jenkins_home/email-templates/

# After starting container in command line run to give docker group necessary permissions:
# docker exec --user root jenkins chgrp docker /var/run/docker.sock
# docker exec --user root jenkins chown -R jenkins:jenkins /var/jenkins_home/workspace/