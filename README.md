# Contract Testing - Tech Talk

*3rd Bikeleasing Tech Talk* <br>
*Date: 2023-12-01* <br>
*Speaker: <a mailto=masotti@bikeleasing.de>Toni Masotti</a>* @antonio-masotti <br>

This repository contains the slides and resources used for the talk about 
Contract Testing.


## Structure 

- `animation/` - Demo Python code to show error propagation in a distributed system
- `slides/` - Slides for the talk
    - `tex/` - The XeTeX / Beamer code used to generate the slides
    - `assets/` - Draw.io files containing the diagrams in the slides
- `resources/` - A selection of literature, videos and tutorials consulted for the talk

## Literature

*see also the [resources](resources/) folder*

**Books**

- Ian Robinson, “[Consumer Driven Contracts - A Service Evolution Pattern](https://martinfowler.com/articles/consumerDrivenContracts.html)”, M. Fowler Blog, 2016
- Aniche, Maurício. *Effective Software Testing: A developer's guide*. Simon and Schuster, 2022.
- Costa, Daniel Nunes Nogueira da. *[Guidelines for Testing Microservice-based Applications](https://recipp.ipp.pt/bitstream/10400.22/21388/1/DM_DanielCosta_2022_MEI.pdf)*. Diss. 2022.
- Meyer, Bertrand. "Touch of class." Learning to program well with Object Technology and Design by Contract, AN INTRODUCTION TO SOFTWARE ENGINEERING (2009).

**Videos**
- Dave Farley, [Contract Testing for Microservices is a MUST](https://www.youtube.com/watch?v=Fh8CqZtghQw)
- Holly Cummins, [Pact Contract Testing for Quarkus](https://www.youtube.com/watch?v=FHNXlOJvCJU)
- J.B. Rainsberger, [Integration Tests are a Scam](https://www.infoq.com/presentations/integration-tests-scam/)

## Tools

- [Pact](https://docs.pact.io/)

## Related Repositories

- See the many [demos and examples](https://github.com/orgs/pactflow/repositories?q=example&type=all&language=&sort=) under pactflow Github organization
- [Terraform Provider Pact](https://github.com/pactflow/terraform-provider-pact)
- [christian-draeger/pact-example](https://github.com/christian-draeger/pact-example)
- [pactflow/example-consumer-js-sns](https://github.com/pactflow/example-consumer-js-sns)
- [mbryia/contract-testing](https://github.com/mbryla/contract-testing)
- [antonio-masotti/tech-talk_contract-testing_sqs-demo](https://github.com/antonio-masotti/tech-talk_contract-testing_sqs-demo) - my own demo for this tech talk
  - *for the nodejs version, see the branch `demo/contract-testing` on the LC repositories*
