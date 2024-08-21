# Questão 7

A Amazon VPN é um serviço que permite conectar redes locais ou privadas à infraestrutura da AWS por meio de uma conexão segura e criptografada. Existem duas principais formas de criar uma VPN na AWS:

AWS Site-to-Site VPN: Conecta redes locais a uma VPC na AWS. Inclui um VPN Gateway na AWS e um Customer Gateway na rede local.
AWS Client VPN: Permite que usuários remotos se conectem com segurança à rede da AWS ou a recursos internos da empresa usando um cliente VPN.

Uma Amazon Subnet é uma subdivisão dentro de uma Amazon VPC que organiza e isola recursos em blocos menores de rede. Ao criar uma VPC, você define um bloco de endereços IP (CIDR) e, dentro dessa VPC, pode criar várias subnets, cada uma com seu próprio intervalo de endereços IP.

### Tipos de Subnets:

**Subnet Pública:** Conectada a um Internet Gateway (IGW), permitindo que recursos como instâncias EC2 se comuniquem diretamente com a internet.
**Subnet Privada:** Não tem acesso direto à internet pública e geralmente usa um NAT Gateway ou NAT Instance para conectividade de saída.

Os Security Groups funcionam como firewalls virtuais para instâncias dentro das subnets na VPC, controlando o tráfego de entrada e saída. Eles permitem definir políticas de segurança específicas para cada recurso, independentemente da subnet em que se encontra. Enquanto as subnets isolam recursos em diferentes níveis de rede, os Security Groups garantem que apenas o tráfego autorizado possa acessar esses recursos.