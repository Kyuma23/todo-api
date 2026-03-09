# frontend/Dockerfile
FROM node:20-alpine

# Criar pasta de trabalho
WORKDIR /app

# Copiar ficheiros de dependências
COPY package*.json ./

# Instalar dependências
RUN npm install

# Copiar o resto do código do Nuxt
COPY . .

# Construir a aplicação Nuxt para produção
RUN npm run build

# Expor a porta 3000
EXPOSE 3000

# Arrancar o servidor Node gerado pelo Nuxt
CMD ["node", ".output/server/index.mjs"]