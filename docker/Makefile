default: build


build:
	docker build --rm -t techiaith/brawddegau-adnabod-lleferydd .


run:
	mkdir -p ${PWD}/data/
	docker run --name techiaith-brawddegau-adnabod-lleferydd \
		--restart=always \
		-it \
		-v ${PWD}/../data/:/data \
		-v ${PWD}/src/:/code \
		-v ${PWD}/homedir/:/root \
		techiaith/brawddegau-adnabod-lleferydd


stop:
	-docker stop techiaith-brawddegau-adnabod-lleferydd
	-docker rm techiaith-brawddegau-adnabod-lleferydd


clean: stop
	-docker rmi techiaith/brawddegau-adnabod-lleferydd

