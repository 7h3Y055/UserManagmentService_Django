



up:
	@docker-compose up --build -d
down:
	@docker-compose down
stop:
	@docker-compose stop
re: down up

ps:
	@docker-compose ps -a
logs:
	docker-compose logs user_managment


shell:
	@docker-compose exec user_managment bash


clean:
	@docker-compose down --rmi all
