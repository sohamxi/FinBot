from crewai import Task
from textwrap import dedent

class InfrastructureManagementTasks:
    def ensure_infrastructure_operates(self, agent, environment):
        return Task(
            description=dedent(f"""\
                [INFRASTRUCTURE OPERATIONAL MANAGEMENT]
                Ensure that the trading infrastructure operates efficiently and reliably in the {environment} environment.

                Responsibilities:
                - Monitor the uptime and responsiveness of API servers, databases, and network connectivity.
                - Perform regular health checks, load testing, and failover validations.
                - Collaborate with IT teams to optimize performance and scalability.
                - Proactively address potential system bottlenecks or vulnerabilities.

                The outputs from this task support continuous operational readiness for live trading.
                """),
            agent=agent
        )

    def monitor_system_performance(self, agent, system_name):
        return Task(
            description=dedent(f"""\
                [SYSTEM PERFORMANCE MONITORING]
                Continuously monitor the performance and resource utilization of the trading system: {system_name}.

                Key metrics to track:
                - CPU, memory, and disk utilization.
                - Network latency, throughput, and API response times.
                - Database performance including query latency and error rates.
                - System logs for anomalies and errors.

                Implement dashboards and log monitoring tools for real-time insights.
                Store performance metrics in:
                - Database Table: system_performance_metrics
                - Log files: /reports/system_monitoring/{system_name}_{{TIMESTAMP}}.json

                This task ensures that performance issues are detected early and addressed promptly.
                """),
            agent=agent
        )

    def implement_automated_alerts(self, agent, environment):
        return Task(
            description=dedent(f"""\
                [AUTOMATED ALERTS SETUP]
                Configure and implement automated alerts for critical events within the trading infrastructure for the {environment} environment.

                Requirements:
                - Define threshold-based triggers for system errors, performance degradation, and downtime.
                - Integrate with incident management systems (e.g., PagerDuty, Slack) to ensure quick response.
                - Test alert workflows and document alert escalation procedures.
                - Ensure alerts provide detailed diagnostic information for rapid troubleshooting.

                Store alert configurations and historical alert logs:
                - Alert System Dashboard
                - Log files: /reports/alerts/{environment}_alerts_{{TIMESTAMP}}.json

                This task enables proactive system management and ensures that critical issues receive immediate attention.
                """),
            agent=agent
        )

    def maintain_system_documentation(self, agent):
        return Task(
            description=dedent(f"""\
                [SYSTEM DOCUMENTATION MANAGEMENT]
                Maintain comprehensive and up-to-date documentation for the entire trading infrastructure and operational processes.

                Documentation should include:
                - Detailed architecture diagrams and component descriptions.
                - API specifications, interface documentation, and inter-service communication protocols.
                - Standard operating procedures (SOP) for deployment, incident response, and system maintenance.
                - Version-controlled change logs and updates.

                Store documentation in a centralized repository accessible to all technical and trading operations teams:
                - Repository Path: /docs/trading_infrastructure/

                This task ensures operational transparency and aids in effective system maintenance and onboarding.
                """),
            agent=agent
        )