import express from 'express'
import pkg from 'pg'

const app = express()

app.use(express.json())

const { Pool } = pkg

const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'avanti',
  password: '1234',
  port: 5432
})

const clientes = [{ id: 1, nome: 'Emily', idade: '18' }]

app.get('/clientes', async (request, response) => {
  const { rows } = await pool.query('SELECT * FROM cliente')
  return response.status(200).json(clientes)
})

app.post('/cliente', (request, response) => {
  // Cria o registro
  const { nome, idade } = request.body
  clientes.push({ nome: nome, idade: idade })
  return response.status(200).json({ nome: nome, idade: idade })
})

app.put('/cliente/:id', (request, response) => {
  const { id } = request.params
  const { nome, idade } = request.body
  clientes.find(c => {
    if (c.id == id) {
      c.nome = nome
      c.idade = idade
    }
  })

  return response.status(201).json({ nome: nome, idade: idade })
})

app.delete('/cliente/:id', (request, response) => {
  const { id } = request.params
  const index = clientes.findIndex(c => c.id == id)
  clientes.splice(index, 1)
  return response.status(204).send()
})

app.listen(3000, () => {
  console.log('Running server')
})
