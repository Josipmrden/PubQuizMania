import { rest } from 'msw'
import { API_URL } from '../apiClient.js'

export default [
  rest.get(`${API_URL}/categories/`, (req, res, ctx) => {
    return res(
      ctx.json(categories)
    )
  }),
  rest.get(`${API_URL}/unlabeled/`, (req, res, ctx) => {
    return res(
      ctx.json(createQuestions(questionNumber))
    )
  }),
  rest.get(`${API_URL}/label/stats/`, (req, res, ctx) => {
    return res(
      ctx.json(stats)
    )
  }),
  rest.post(`${API_URL}/label/`, (req, res, ctx) => {
      questionNumber += 1
      return res(
          ctx.status(200)
      )
  }),
  rest.post(`${API_URL}/random_quiz/`, (req, res, ctx) => {
    return res(
        ctx.json(quiz)
    )
})
]

const categories = {
    'categories': [
        {
            'name': 'CATEGORY 1',
            'abbrev': 'C1',
        },
        {
            'name': 'CATEGORY 2',
            'abbrev': 'C2',
        },
        {
            'name': 'CATEGORY 3',
            'abbrev': 'C3',
        },
        {
            'name': 'CATEGORY 4',
            'abbrev': 'C4',
        }
    ]
}

var questionNumber = 1
var createQuestions = (number) => {
    return {
        'unlabeled_questions': [
            {
                'number' : number,
                'question': `Q${number}`,
                'answer': `A${number}`,
                'categories' : []
            },
            {
                'number' : number + 1,
                'question': `Q${number + 1}`,
                'answer': `A${number + 1}`,
                'categories' : []
            },
            {
                'number' : number + 2,
                'question': `Q${number + 2}`,
                'answer': `A${number + 2}`,
                'categories' : []
            },
            {
                'number' : number + 3,
                'question': `Q${number + 3}`,
                'answer': `A${number + 3}`,
                'categories' : []
            },
        ]
    }
}

const stats = {
    'labeled_questions': 1,
    'total_questions': 100
}

const quiz = {
    'questions': [
        {
            'number': 1,
            'question': "Pitanje broj 1"
        },
        {
            'number': 2,
            'question': "Pitanje broj 2"
        },
        {
            'number': 3,
            'question': "Pitanje broj 3 Pitanje broj 3 Pitanje broj 3 Pitanje broj 3 Pitanje broj 3 Pitanje broj 3"
        },
        {
            'number': 4,
            'question': "Pitanje broj 4"
        },
        {
            'number': 5,
            'question': "Pitanje broj 1"
        },
        {
            'number': 6,
            'question': "Pitanje broj 2"
        },
        {
            'number': 7,
            'question': "Pitanje broj 3 Pitanje broj 3 Pitanje broj 3 Pitanje broj 3 Pitanje broj 3 Pitanje broj 3"
        },
        {
            'number': 8,
            'question': "Pitanje broj 4"
        },
        {
            'number': 9,
            'question': "Pitanje broj 1"
        },
        {
            'number': 10,
            'question': "Pitanje broj 2"
        },
        {
            'number': 11,
            'question': "Pitanje broj 3 Pitanje broj 3 Pitanje broj 3 Pitanje broj 3 Pitanje broj 3 Pitanje broj 3"
        },
        {
            'number': 12,
            'question': "Pitanje broj 4"
        },
        {
            'number': 13,
            'question': "Pitanje broj 1"
        },
        {
            'number': 14,
            'question': "Pitanje broj 2"
        },
        {
            'number': 15,
            'question': "Pitanje broj 3 Pitanje broj 3 Pitanje broj 3 Pitanje broj 3 Pitanje broj 3 Pitanje broj 3"
        },
        {
            'number': 16,
            'question': "Pitanje broj 4"
        },
        {
            'number': 17,
            'question': "Pitanje broj 1"
        },
        {
            'number': 18,
            'question': "Pitanje broj 2"
        },
        {
            'number': 19,
            'question': "Pitanje broj 3 Pitanje broj 3 Pitanje broj 3 Pitanje broj 3 Pitanje broj 3 Pitanje broj 3"
        },
        {
            'number': 20,
            'question': "Pitanje broj 4"
        },
    ]   
}