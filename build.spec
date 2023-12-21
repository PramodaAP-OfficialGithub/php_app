version: 0.2
phases:
  install:
    commands:
      - echo installing httpd
      - sudo yum update -y
      - sudo yum install httpd -y
  build:
    commands:
      - cp index.php /var/www/html
  post_build:
    commands:
      - echo configuring httpd
artifacts:
  files:
    - /var/www/html/index.php
