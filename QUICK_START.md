# Quick Start Guide 🚀

Welcome to LeetcodeSess! This guide will help you get started with documenting your LeetCode journey.

## Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/LeetcodeSess.git
cd LeetcodeSess
```

> **Note:** Replace `YOUR-USERNAME` with your actual GitHub username.

## Step 2: Start Your First Session

1. **Create a session log:**
   ```bash
   cp templates/session_template.md sessions/$(date +%Y-%m-%d).md
   ```

2. **Edit the session file** with your text editor and fill in:
   - Session goals
   - Duration
   - Focus area

## Step 3: Document a Problem

1. **Create a new problem document:**
   ```bash
   # For an easy problem
   cp templates/problem_template.md problems/easy/problem-name.md
   
   # For a medium problem
   cp templates/problem_template.md problems/medium/problem-name.md
   
   # For a hard problem
   cp templates/problem_template.md problems/hard/problem-name.md
   ```

2. **Fill in the problem document:**
   - Problem description
   - Your approach and thought process
   - Solution code (with proper syntax highlighting)
   - Test cases
   - Lessons learned

3. **Use consistent naming:**
   - Use lowercase with hyphens: `two-sum.md`, `binary-tree-traversal.md`
   - Include problem number if helpful: `001-two-sum.md`

## Step 4: Update Progress

After solving problems, update the README.md:

1. Add the problem to the appropriate table (Easy/Medium/Hard)
2. Update the statistics section
3. Add the session to the Study Sessions table
4. Update topic counts

## Step 5: Commit Your Work

```bash
git add .
git commit -m "Add [problem name] solution and session log"
git push
```

## Tips for Effective Documentation

### Writing Problem Solutions

- **Be detailed in your approach:** Future you will thank present you
- **Include multiple approaches:** Compare trade-offs
- **Add visual aids:** Diagrams, examples, or step-by-step walkthroughs
- **Tag properly:** Use consistent tags for easy searching

### Logging Sessions

- **Be honest about struggles:** Document what was difficult
- **Track time spent:** Helps identify areas needing more practice
- **Reflect meaningfully:** What did you learn? What would you do differently?
- **Set clear goals:** Both for current and next sessions

### Staying Consistent

- **Daily practice:** Even 30 minutes makes a difference
- **Review old problems:** Spaced repetition helps retention
- **Follow patterns:** Recognize common problem-solving patterns
- **Track progress:** Celebrate milestones

## Example Workflow

Here's a typical workflow for a study session:

```bash
# 1. Create today's session file
cp templates/session_template.md sessions/2024-01-15.md

# 2. Open LeetCode and pick a problem

# 3. Solve the problem (on LeetCode or locally)

# 4. Document the solution
cp templates/problem_template.md problems/medium/container-with-most-water.md

# 5. Fill in both files with your work

# 6. Update README.md progress tables

# 7. Commit everything
git add .
git commit -m "Session 2024-01-15: Container With Most Water"
git push
```

## Folder Structure Reference

```
LeetcodeSess/
├── problems/
│   ├── easy/               # Easy difficulty problems
│   │   └── two-sum.md     # Example problem
│   ├── medium/            # Medium difficulty problems
│   └── hard/              # Hard difficulty problems
├── sessions/              # Study session logs
│   └── 2024-01-01-example.md  # Example session
├── templates/             # Templates for new entries
│   ├── problem_template.md    # Problem documentation template
│   └── session_template.md    # Session log template
├── .gitignore
├── QUICK_START.md        # This file
└── README.md             # Main documentation
```

## Common Issues

### Problem: Too many files to update

**Solution:** Create a simple script or use a checklist to remember all the places to update (problem file, session log, README tables).

### Problem: Forgetting to document

**Solution:** Make documentation part of the problem-solving process, not an afterthought. Document as you go.

### Problem: Inconsistent naming

**Solution:** Always use the templates and follow the naming convention: lowercase with hyphens.

## Resources

- Check out the [example problem](problems/easy/two-sum.md) to see how to document
- Review the [example session](sessions/2024-01-01-example.md) for session logging
- Read the main [README](README.md) for the complete overview

---

Happy coding! 🎯
